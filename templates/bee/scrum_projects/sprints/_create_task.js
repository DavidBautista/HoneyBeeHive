console.info("task created");
(function(){
  if('{{reset_dom}}'=='true'){
    $('#tasks').html("");
  }
  var templ = _.template($('#task-overview-template').html());
  var datas={'name':"{{new_task.name}}", 'username':'{{new_task.assigned_user.name}}',
    'pred_start_date':'{{new_task.pred_start_date|date:"SHORT_DATE_FORMAT"}}',
    'pred_end_date':'{{new_task.pred_end_date|date:"SHORT_DATE_FORMAT"}}', 'time_prevision':"{{new_task.time_prevision}}",
  'id':"{{new_task.id}}", 'description':'{{new_task.description}}', 'status':'{{new_task.status}}', 'time_worked':'{{new_task.time_worked}}'};
  $("#tasks").append((templ(datas)));
  $.colorbox.close();
})();
