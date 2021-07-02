var platform = new H.service.Platform({
  'apikey': '-igx-K35_7339M64eO-YBL5SnUS5G0k1AHKKW7-Ab6E'
});

var defaultLayers = platform.createDefaultLayers();

var map = new H.Map(document.getElementById('mapContainer'),
            defaultLayers.vector.normal.map,
            {
                zoom: 14,
                pixelRatio: window.devicePixelRatio || 1
            });

window.addEventListener('resize', () => map.getViewPort().resize());

var ui = H.ui.UI.createDefault(map, defaultLayers);

var mapEvents = new H.mapevents.MapEvents(map);
var behavior = new H.mapevents.Behavior(mapEvents);

var service = platform.getSearchService();

function addMarkerToGroup(group, coordinate, html, icon) {
  var marker = new H.map.DomMarker(coordinate, icon);
  marker.setData(html);
  group.addObject(marker);
}

function centerMap(position) {
  console.log(position);
  map.setCenter({lat: position.coords.latitude, lng: position.coords.longitude});
  var pos = new H.map.Marker({lat: position.coords.latitude, lng: position.coords.longitude});
  map.addObject(pos)
  $("#lat").val(position.coords.latitude);
  $("#lng").val(position.coords.longitude);
}

function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(centerMap);
  } else {
    map.setCenter({lat: -33.46468, lng: -70.65655});
  }
}

var tiempo, focusbuscar, focuslista;

$(function () {
  getLocation();

  $("#checkCercanos").change(function() {
    $(this).val($(this).is(':checked'));
    $("#form_buscar").submit();
  });

	$("#buscar").focusout(function() {
		setTimeout(function(){
			focusbuscar = false;
			if (!focusbuscar && !focuslista) {
				clearTimeout(tiempo);
				$('#listabuscar').dropdown('hide');
			}
		},100);
	});

	$("#listabuscar").focusout(function() {
		setTimeout(function(){
			focuslista = false;
			if (!focusbuscar && !focuslista) {
				clearTimeout(tiempo);
				$('#listabuscar').dropdown('hide');
			}
		},100);
	});

	$("#buscar").focus(function() {
		focusbuscar = true;
	});

	$("#listabuscar").focus(function() {
		focusbuscar = true;
	});

	$("#buscar").on('keyup', function() {
		if ( event.which == 13 ) {
			agotado();
		}
		clearTimeout(tiempo);
		tiempo = setTimeout(agotado, 1000);
	});

	$("#buscar").on('keydown', function() {
	  clearTimeout(tiempo);
	  $('#listabuscar').dropdown('hide');
	});
})

function agotado() {
  clearTimeout(tiempo);
  let texto = $("#buscar").val().trim();
  let check = $("#checkCercanos").val().trim();
  let lat = $("#lat").val().trim();
  let lng = $("#lng").val().trim();

  if(texto.length == 0) return false;

  $.post("../../deportivas/buscar", {
      buscar:texto,
      cercanos:check,
      lat,
      lng
    },function(data){
      console.log(data);
      $("#listabuscar").empty();
    for (resultado of data) {
      $("#listabuscar").append('<button class="dropdown-item" onclick="$(\'#buscar\').val(\'' + resultado["nombre"] + '\'); $(\'#form_buscar\').submit()">' + resultado["nombre"] + '</button>')
    }
    if (data.length == 0) {
      $("#listabuscar").append('<button disabled class="dropdown-item">No hay resultados</button>')
    }
    });
  $('#listabuscar').addClass('show');
  $('#listabuscar').dropdown('show');
}

