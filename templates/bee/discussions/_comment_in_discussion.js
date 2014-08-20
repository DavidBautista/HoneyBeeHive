console.info("commented");

(function(){
  var templ = _.template($('#post-overview-template').html());
  var datas = {'sendername':"{{new_post.sender.name}}", 'date':"{{ new_post.date|date:'SHORT_DATETIME_FORMAT' }}", 'content':"{{new_post.content}}"};
  $("#posts-list").append((templ(datas)));

})();
