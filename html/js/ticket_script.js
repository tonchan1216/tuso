$(function() {
	//block →　seat
	$("#ticket-seat article > div").hide();
	$('#ticket-block .seat-block').click(function() {
		$('#ticket-block').removeClass('active').removeClass('in');
		$('#ticket-seat').addClass('active').addClass('in');
		$('#ticket-menu li').removeClass('active');
		$('#ticket-menu li:nth-child(2)').addClass('active');

		$('#ticket-seat .'+$(this).data('position')).fadeIn();
	})

	//seat select
	$('#ticket-seat .seat').click(function() {
		$(this).toggleClass('selected');
		$column = $(this).text();
		$row = $(this).parent().children('th').text();
		$selected_seat = $row + "-" + $column;
		if ($row > 20) {
			$floor = "3階";
		}else{
			$floor = "2階";
		}

		$exist_flag = false;
		$('#ticket-confirm .selected-seat').each(function (i, e){
			if ($(e).text() == $selected_seat) {
				$(e).parent().remove();
				$exist_flag = true;			
			}
		})

		if (!$exist_flag) {
			$('#ticket-confirm table tbody').append('<tr><td>'+$floor+'</td><td class="selected-seat">'+$selected_seat+'</td>	</tr>');
		}
	})


	//	seat →　confirm
	$('#ticket-seat button').click(function() {
		$('#ticket-seat').removeClass('active').removeClass('in');
		$('#ticket-menu li').removeClass('active');
		$("#ticket-seat article > div").hide();
		if ($(this).val() == 'back') {
			$('#ticket-block').addClass('active').addClass('in');
			$('#ticket-menu li:nth-child(1)').addClass('active');
		}	else {
			$('#ticket-confirm').addClass('active').addClass('in');
			$('#ticket-menu li:nth-child(3)').addClass('active');

			$('#ticket-confirm .seat-sum').text($('#ticket-confirm .selected-seat').length + '枚');
		}
	})

	//confirm　→　form
	$('#ticket-confirm button').click(function() {
		$('#ticket-confirm').removeClass('active').removeClass('in');
		$('#ticket-menu li').removeClass('active');
		if ($(this).val() == 'back') {
			$('#ticket-block').addClass('active').addClass('in');
			$('#ticket-menu li:nth-child(1)').addClass('active');
		}	else {
			$('#ticket-form').addClass('active').addClass('in');
			$('#ticket-menu li:nth-child(4)').addClass('active');
		}
	})
});

