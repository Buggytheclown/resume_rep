// post voting with server response
$('form.voteForm').submit(function () {
    $.post(
        '/', // ссылка куда отправляем данные
        $(this).serialize() // данные формы
    ).done(function (data) {
        var rating_id = '#rating_' + data.post_id;
        var rate = ' ' + data.rating;
        $(rating_id).fadeOut(300, function () {
            $(this).text(rate).fadeIn(300);  // for unreg user??
        });
    });
    // отключаем действие по умолчанию
    return false;
});


// change voting button color
$('.just-glyph.plus')
    .on('mouseenter', function () {
        $(this).children('i').addClass('voteup')
    })
    .on('mouseleave', function () {
        if ($(this).parents('div.forVote').data('voted') !== 'plus') {
            $(this).children('i').removeClass('voteup')
        }
    });

$('.just-glyph.minus')
    .on('mouseenter', function () {
        $(this).children('i').addClass('votedown')
    })
    .on('mouseleave', function () {
        if ($(this).parents('div.forVote').data('voted') !== 'minus') {
            $(this).children('i').removeClass('votedown')
        }
    });

$('.just-glyph.minus')
    .on('click', function () {
        var pdiv = $(this).parents('div.forVote');
        if (pdiv.data('voted') === 'plus') {
            pdiv.data('voted', '');
        } else {
            pdiv.data('voted', 'minus')
        }
        pdiv.find('.plus').children('i').removeClass('voteup');
    });

$('.just-glyph.plus')
    .on('click', function () {
        var pdiv = $(this).parents('div.forVote');
        if (pdiv.data('voted') === 'minus') {
            pdiv.data('voted', '');
        } else {
            pdiv.data('voted', 'plus')
        }
        pdiv.find('.minus').children('i').removeClass('votedown');
    });


// mail_to hidden
$('i.mail_to').on('click', function (event) {
    var userid = $(this).data('userid');
    var postid = '#' + 'mail_' + $(this).data('postid');
    var $mydiv = $(postid);
    //var mydivY = event.pageY - $mydiv.css('height').slice(0,-2) + 10 + 'px';
    //var mydivX = event.pageX - 10 + 'px';
    //$mydiv.css({'top': mydivY,
    //            'left': mydivX});
    $mydiv.slideDown('fast');
    return false
});


$('input.closeMail').on('click', function (event) {
    $(this).parents('div.mailForm').slideUp('fast').find('textarea').val('');
});

$('form.mailForm').submit(function () {
    var action = '/' + $(this).data('id') + '/' + 'mail_to' + '/';
    $.post(
        action, // ссылка куда отправляем данные
        $(this).serialize() // данные формы
    );
    //.done(function (data) {
    //    var rating_id = '#rating_' + data.post_id;
    //    var rate = ' ' + data.rating;
    //    $(rating_id).fadeOut(300, function () {
    //        $(this).text(rate).fadeIn(300);  // for unreg user
    //    });
    //});
    // отключаем действие по умолчанию
    $(this).parents('div.mailForm').slideUp('fast').find('textarea').val('');
    return false;
});
