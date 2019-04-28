// window.onload = function () {
//     $(".basket_list").on("change", "input[type='number']", function (event) {
//         let target = event.target;
//         $.ajax({
//             url: "/basket/edit/" + target.name + "/" + target.value + "/",
//             success: function (data) {
//                 $('.basket_list').html(data.result);
//             }
//         });
//     });
// };


window.onload = function () {
    $('.basket_list').on('click', 'input[type="number"]', function () {
        var t_href = event.target;

        $.ajax({
            url: "/basket/edit/" + t_href.name + "/" + t_href.value,
            success: function (data) {
                $('.basket_list').html(data.result);
            }
        });

        event.preventDefault();
    });
};