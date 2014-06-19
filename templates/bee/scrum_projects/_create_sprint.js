$(function(){
  if('{{reset_dom}}'=='true'){
    $('#sprints').html("");
  }
  var templ = _.template($('#sprint-overview-template').html());
  var datas={'name':"{{sprint.name}}"};
  $("#sprints").append((templ(datas)));
  $.colorbox.close();
})();
