console.info("task created");
$(function(){
  if('{{reset_dom}}'=='true'){
    $('#tasks').html("");
  }
  var templ = _.template($('#task-overview-template').html());
  var datas={'name':"{{sprint.name}}", 'id':"{{sprint.id}}"};
  $("#sprints").append((templ(datas)));
  $.colorbox.close();
})();
