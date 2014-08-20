
var SprintTasks = (function () {
  var self = {};
  self.resetDom = false;
  self.Task = Backbone.Model.extend();
  self.Tasks = Backbone.Collection.extend({
    parse: function (resp) {
      this.meta = resp.meta;
      return resp.objects;
    },
    model: self.Task,
    url: '/api/bee/0.1.0/task/'
  });
  self.TaskView = Backbone.View.extend({
    tagName: 'div',
    template: _.template($('#task-overview-template').html()),
    render: function () {
      this.$el.html(this.template(
          this.model.toJSON()
      ));
      return this;
    }
  });

  self.TasksCallView = Backbone.View.extend({
    initialize: function () {
      _.bindAll(this, 'renderRows', 'renderInfo');
      this.tasks = new self.Tasks();
      this.tasks.on('sync', this.renderRows, this);
      this.$el.html("");
    },

    renderRows: function (rows) {
      if(rows.length==0)
        this.noData();
      else
        rows.each(this.renderInfo);
    },

    renderInfo: function (rep) {
      console.info("renderinfo", rep);
      var view = new self.TaskView({
        model: rep
      });
      this.$el.append(view.render().el);
    },
    noData: function(){
      this.$el.append($('#no-tasks-in-sprint').html());
      self.resetDom = true;
      try {
        $(".create-task-link").colorbox({innerHeight:600,scrolling:false});
      } catch (Exception) {}
    },
    load: function (data) {
      this.tasks.fetch({
        reset: true,
        data: data,
        type: "GET",
        success: function (model, resp) {
          console.info('Fetched tasks', model, resp);
        },
        error: function (model, resp) {
          console.error('Could not load tasks', model, resp);
        }
      });
    }

  });

  return self;
});

$(document).ready(function() {
  SprintTasks = SprintTasks();
});