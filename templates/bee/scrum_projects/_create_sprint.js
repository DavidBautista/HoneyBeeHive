(function(){
  if('{{reset_dom}}'=='true'){
    $('#sprints').html("");
  }
  var templ = _.template($('#sprint-overview-template').html());
  var datas={'name':"{{sprint.name}}", 'id':"{{sprint.id}}", 'start_date_f':'{{sprint.start_date_f|date:"SHORT_DATE_FORMAT"}}',
    'end_date_f':'{{sprint.end_date_f|date:"SHORT_DATE_FORMAT"}}', 'num_discussions':"{{sprint.num_discussions}}", 'num_tasks':"{{sprint.num_tasks}}",
    'num_tasks_completed':"{{sprint.num_tasks_completed}}"};
  $("#sprints").append((templ(datas)));
  $.colorbox.close();
})();
