require('datatables.net');

$(document).ready( function () {
	let $form = $("form#history");
	let $results = $("div#results");
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


	$("#id_requests").on('change', function (e) {
		let value = $(this).find('option:selected').val();

		e.preventDefault();
		$.ajax({
			type: "GET",
			url: $form.attr('action') + value,
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

				$results.show();
				$('#results-counter').html(results.stats);
				$('#results-keyword').html(data.keyword);
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
	$("#id_requests option:selected").prop("selected", false)
});
