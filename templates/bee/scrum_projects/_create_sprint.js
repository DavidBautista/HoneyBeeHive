(function(){
  if('{{reset_dom}}'=='true'){
    $('#sprints').html("");
  }
  var templ = _.template($('#sprint-overview-template').html());
  var datas={'name':"{{sprint.name}}", 'id':"{{sprint.id}}"};
  $("#sprints").append((templ(datas)));
  $.colorbox.close();
})();
