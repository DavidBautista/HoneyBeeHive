
var ProjectSprints = (function () {
  var self = {};
  self.Sprint = Backbone.Model.extend();
  self.Sprints = Backbone.Collection.extend({
    parse: function (resp) {
      this.meta = resp.meta;
      return resp;
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
      rows.each(this.renderInfo);
    },

    renderInfo: function (rep) {
      console.info("renderinfo", rep);
      rep.attributes.lines_list = self.lines_list;
      rep.attributes.lines_units = self.lines_units;
      var view = new self.SprintView({
        model: rep
      });
      this.$el.append(view.render().el);
    },

    load: function (data) {
      this.sprints.fetch({
        reset: true,
        data: data,
        type: "GET",
        success: function () {
          console.info('Fetched sprints');
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

// data['csrfmiddlewaretoken'] = data[0]['csrfmiddlewaretoken'];
//            for (i = 0; i < formdom.length; i++) {
//                data[i] = JSON.stringify(data[i]);
//            }
//var callview= new window.marenostrum.simulator1vs1.SimulationReportCallView({el:"#battle_result"});
//            callview.load(data);