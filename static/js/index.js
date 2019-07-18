require('datatables.net');

function hide_alert_on_input(input) {
	if(input.val() == ""){
		if ($('.alert-search').is(":hidden")) {
			$('.alert-search').show();
		} 
	} else {
		$('.alert-search').hide();
	}
}

$(document).ready( function () {
	let $form = $("form#search");
	let $results = $("div#results");
	let $search_input = $form.find('input#id_keyword');
	let $submit_btn = $form.find('input[type="submit"]');
	let config = {
		"searching": false,
		"lengthChange": false,
		"info": false,
		"paging": false,
		"language": {
			"search": ""
		}
	}
	let popular_config = {
		"order": [[1, "desc"]]
	}

	let $serp_table = $('table#serp');
	let $serp_table_dt = $serp_table.DataTable(config);

	let $popular_table = $('table#popular');
	let $popular_table_dt = $popular_table.DataTable(Object.assign({}, config, popular_config));

	$form.submit(function (e) {
		e.preventDefault();
		let data = $form.serializeArray();
		$.ajax({
			type: "POST",
			url: $form.attr('action'),
			data: $form.serializeArray(),
			beforeSend: function () {
				$('div.loading').show();
			},
			success: function(data)
			{
				let results = JSON.parse(data.results);
				$serp_table_dt.clear().draw();
				$serp_table_dt.rows.add(results.serp);
				$serp_table_dt.draw();

				$popular_table_dt.clear().draw();
				$popular_table_dt.rows.add(results.popular);
				$popular_table_dt.draw();

				$('#results-counter').html(results.stats);
				$('#results-keyword').html(data.keyword);
				if (data.cache) {
					$('#cache-results').show()
				} else {
					$('#cache-results').hide()
				}
				$("#ua-string").html(data.user_agent);

				$results.show();
			},
			error: function(data)
			{
				console.log(data);
			},
			complete: function () {
				$('div.loading').hide();
			}
		});
	});

	$search_input.keyup(function () {
		hide_alert_on_input($search_input);
	});
	hide_alert_on_input($search_input);
} );
