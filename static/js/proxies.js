import '@fortawesome/fontawesome-free/js/fontawesome'
import '@fortawesome/fontawesome-free/js/solid'
import '@fortawesome/fontawesome-free/js/regular'
import '@fortawesome/fontawesome-free/js/brands'

require('datatables.net');

$(document).ready(function() {

	function getCookie(name) {
		var cookieValue = null;
		if (document.cookie && document.cookie !== '') {
			var cookies = document.cookie.split(';');
			for (var i = 0; i < cookies.length; i++) {
				var cookie = cookies[i].trim();
				// Does this cookie string begin with the name we want?
				if (cookie.substring(0, name.length + 1) === (name + '=')) {
					cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
					break;
				}
			}
		}
		return cookieValue;
	}

	function init_event_handlers() {

		$table.on('click', 'button.delete-proxy', function (e) {
			e.preventDefault();
			let that = $(this);
			let url = that.data('url');
			let csrftoken = getCookie('csrftoken');

			$.ajax({
				type: "DELETE",
				url: url,
				beforeSend: function(xhr, settings) {
					xhr.setRequestHeader("X-CSRFToken", csrftoken);
				},
				success: function(data) {
					var tr = that.closest('tr')
					console.log(that)
					console.log(e)
					tr.remove();
				}
			});
		});

		$form.on('submit', function (e) {
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
					$table_dt.ajax.reload()
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

	}

	let $form = $("form#proxies");
	let config = {
		"searching": false,
		"lengthChange": false,
		"info": false,
		"paging": false,
		"language": {
			"search": ""
		},
		"sAjaxDataProp": "",
		ajax: {
			url: $("#table-proxies").data('url'),
			processing: true
		},
		columns: [
			{"data": "proxy_url"},
			{"data": "proxy_buttons"}
		]
	}

	let $table = $('#table-proxies');
	let $table_dt = $table.DataTable(config);

	init_event_handlers();
});