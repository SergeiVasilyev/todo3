$(document).ready(function() {
    // Функция кнопки CATEGORY EDIT, выводит поле с форомой Input
    // И получает текущее значение todoitem из базы данных
    $('.edit_cat_btn').click(function(){
        console.log('CLICK A ' + $(this).attr("id_a"))
        var idx = $(this).attr("id_a")
        //console.log($('#' + idx).hasClass("list-group-item-strikethrough"))
        if (!$('#' + idx).hasClass("list-group-item-strikethrough")){
          $('#block_edit_'+idx).toggle("fast")
        }
        // Не нужно, так как получаем данные из джанго напрямую в шаблон
        // $.get('data_update_cat_form/'+idx+'/', function (data, status) {
        //   console.log(data)
        //   $('#block_edit_'+idx+' form input').val(data.todoitem)
        //   $('#block_edit_'+idx+' form textarea').val(data.todo_description)
        // });
      })
})