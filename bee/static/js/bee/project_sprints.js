
var ProjectSprints = (function () {
  var self = {};
  self.resetDom = false;
  self.Sprint = Backbone.Model.extend();
  self.Sprints = Backbone.Collection.extend({
    parse: function (resp) {
      this.meta = resp.meta;
      return resp.objects;
    },
    model: self.Sprint,
    url: '/api/bee/0.1.0/sprint/'
  });
  self.SprintView = Backbone.View.extend({
    tagName: 'div',
    template: _.template($('#sprint-overview-template').html()),
    render: function () {
      this.$el.html(this.template(
          this.model.toJSON()
      ));
      return this;
    }
  });

  self.SprintsCallView = Backbone.View.extend({
    initialize: function () {
      _.bindAll(this, 'renderRows', 'renderInfo');
      this.sprints = new self.Sprints();
      this.sprints.on('sync', this.renderRows, this);
      this.$el.html("");
    },

    renderRows: function (rows) {
      if(rows.length==0)
        this.noData();
      else
        rows.each(this.renderInfo);
    },

    renderInfo: function (rep) {
      //console.info("renderinfo", rep);
      var view = new self.SprintView({
        model: rep
      });
      this.$el.append(view.render().el);
    },
    noData: function(){
      this.$el.append($('#no-sprints-in-project').html());
      self.resetDom = true;
      try {$("#create_sprint-link").colorbox({innerHeight:300, scrolling:false});} catch (Exception) {}
    },
    load: function (data) {
      this.sprints.fetch({
        reset: true,
        data: data,
        type: "GET",
        success: function (model, resp) {
          console.info('Fetched sprints', model, resp);
        },
        error: function (model, resp) {
          console.error('Could not load sprints', model, resp);
        }
      });
    }

  });

  return self;
});

$(document).ready(function() {
  ProjectSprints = ProjectSprints();
});
