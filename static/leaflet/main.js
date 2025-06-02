document.addEventListener('DOMContentLoaded', function() {
    // راه‌اندازی نقشه
    var map = L.map('map', {
        zoomControl: false // غیرفعال کردن دکمه زوم
    }).setView([35.1054, 53.6405], 5);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    // متغیر برای نگه‌داری نشانگر
    var marker = null;

    // گرفتن توکن CSRF از HTML
    var csrfToken = document.getElementById('csrf_token').value;

    // فرم برای ارسال مختصات
    var form = document.createElement('form');
    form.method = 'POST';
    form.innerHTML = '<input type="hidden" name="csrfmiddlewaretoken" value="' + csrfToken + '"><input type="hidden" name="latitude" id="latitude"><input type="hidden" name="longitude" id="longitude">';
    document.body.appendChild(form);

    // گرفتن مختصات با کلیک
    map.on('click', function(e) {
        var lat = e.latlng.lat.toFixed(4);
        var lng = e.latlng.lng.toFixed(4);
        document.getElementById('latlng').textContent = lat + ', ' + lng;

        // حذف نشانگر قبلی
        if (marker) {
            map.removeLayer(marker);
        }
        // اضافه کردن نشانگر جدید
        marker = L.marker([lat, lng]).addTo(map);

        // ارسال مختصات به سرور
        document.getElementById('latitude').value = lat;
        document.getElementById('longitude').value = lng;
        form.submit();
    });
});




// var map = L.map('map').setView([35.1054, 53.6405 ], 5); 
// L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
//     attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
// }).addTo(map);

// // متغیر برای نگه‌داری نشانگر
// var marker = null;

// // گرفتن مختصات با کلیک
// map.on('click', function(e) {
//     var lat = e.latlng.lat.toFixed(4);
//     var lng = e.latlng.lng.toFixed(4);
//     document.getElementById('latlng').textContent = lat + ', ' + lng;

//     // حذف نشانگر قبلی (اگه وجود داشته باشه)
//     if (marker) {
//         map.removeLayer(marker);
//     }
//     // اضافه کردن نشانگر جدید
//     marker = L.marker([lat, lng]).addTo(map);
// });



// L.control.zoom({
//     position: 'bottomright'
// }).addTo(map);


