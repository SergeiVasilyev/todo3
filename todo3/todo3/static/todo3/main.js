$(document).ready(function() {

    // AJAX функция, помечает элемент зеленым изменяя класс li 
    // и отправляет на сервер запрос для изменения в бпзе данных поля tofoitem_fav
    document.querySelector('.list-group').onclick = function (event) {
      //console.log($(event.target).attr("id"));
      //console.log(event.target);
      var idx = $(event.target).attr("id");
      if(!$(event.target).hasClass('list-group-item-strikethrough') && $(event.target).is('li')){
        $.post('mark_item/'+idx+'/', function (data, status) {
          console.log('data ' + data);
          $('#' + idx).toggleClass('list-group-item-success list-group-item-light');
        });
      };
    }

    // Функция кнопки EDIT, выводит поле с форомой Input
    // И получает текущее значение todoitem из базы данных
    $('.edit_btn').click(function(){
      console.log('CLICK A ' + $(this).attr("id_a"))
      var idx = $(this).attr("id_a")
      //console.log($('#' + idx).hasClass("list-group-item-strikethrough"))
      if (!$('#' + idx).hasClass("list-group-item-strikethrough")){
        $('#block_edit_'+idx).toggle("fast")
      }
      $.get('data_update_form/'+idx+'/', function (data, status) {
        console.log(data)
        $('#block_edit_'+idx+' form input').val(data.todoitem)
        $('#block_edit_'+idx+' form textarea').val(data.todo_description)
      });
    })
    
    // Функция открытия блока с описанием, по нажатию кнопки со стрелкой
    $('.description_btn').click(function(){
      var idx = $(this).attr("id_edit_a")
      if (!$('#' + idx).hasClass("list-group-item-strikethrough")){
        $('#block_description_'+idx).toggle("fast")
        console.log ($(this).find("i").attr('class'))
        $(this).find("i").toggleClass("bi-caret-down bi-caret-left")
      }
    })

    // Функция изменяя классы и css переносит кнопки списка дел на новую строку, если экран меньше 500px
    // а также изменяет padding & margin
    checkWidth(); // проверит при загрузке страницы
    $(window).resize(function(){
      checkWidth(); // проверит при изменении размера окна клиента
    })
    function checkWidth() {
      var windowWidth = $('body').innerWidth(),
        elem = $(".list-group li");
        elem_div = $(".list-group li div");
        console.log('paddingTop ' + elem_div.css('paddingTop'))
      if(windowWidth < 500){
        elem.removeClass('align-items-center');
        elem.addClass('flex-column');
        elem.addClass('align-items-start');
        elem_div.css('marginTop', '0.8em')
        elem_div.css('marginBottom', '0.4em')
      }
      else{
        elem.removeClass('flex-column');
        elem.addClass('align-items-center');
        elem_div.css('marginTop', '0em')
        elem_div.css('marginBottom', '0em')
      }
    }
    
    // Добавить обработку нажатия кнопку ВЫПОЛНЕНО в DJANGO, не в javascript
    // Плюс сдеалть серыми остальные кнопки, при нажатии на кнопку СДЕЛАНО
    // Сделать TEMPLATE для формы
  })