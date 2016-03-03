$(function() {
	//block →　seat
	$("#ticket-seat article > div").hide();
	$('#ticket-block .seat-block').click(function() {
		$('#ticket-block').removeClass('active').removeClass('in');
		$('#ticket-seat').addClass('active').addClass('in');
		$('#tab-menu li').removeClass('active');
		$('#tab-menu li:nth-child(2)').addClass('active');

		$('#ticket-seat .'+$(this).data('position')).fadeIn();

		//at seat
		switch ($(this).data('position')){
			case 'second-forward':
			$row = 16;
			$column = 5;
			break;
			case 'second-center':
			$row = 16;
			$column = 9;
			break;
			case 'second-left':
			$row = 16;
			$column = 5;
			break;
			case 'second-right':
			$row = 16;
			$column = 5;
			break;
			case 'third-center':
			$row = 13;
			$column = 6;
			break;
			case 'third-left':
			$row = 11;
			$column = 6;
			break;
			case 'third-right':
			$row = 11;
			$column = 6;
			break;
		}
	})

	//	seat →　confirm
	$('#ticket-seat button').click(function() {
		$('#ticket-seat').removeClass('active').removeClass('in');
		$('#tab-menu li').removeClass('active');
		$("#ticket-seat article > div").hide();
		if ($(this).val() == 'back') {
			$('#ticket-block').addClass('active').addClass('in');
			$('#tab-menu li:nth-child(1)').addClass('active');
		}	else {
			$('#ticket-confirm').addClass('active').addClass('in');
			$('#tab-menu li:nth-child(3)').addClass('active');
		}
	})

	//confirm　→　form
	$('#ticket-confirm button').click(function() {
		$('#ticket-confirm').removeClass('active').removeClass('in');
		$('#tab-menu li').removeClass('active');
		if ($(this).val() == 'back') {
			$('#ticket-seat').addClass('active').addClass('in');
			$('#tab-menu li:nth-child(2)').addClass('active');
		}	else {
			$('#ticket-form').addClass('active').addClass('in');
			$('#tab-menu li:nth-child(4)').addClass('active');
		}
	})
});

