
document.getElementById("registration_form").addEventListener("submit", function registrate(){

    alert('here');

    $.ajax({
        data: {
            "email": "string",
            "password": "string",
            "is_active": true,
            "is_superuser": false,
            "is_verified": false,
            "name": "string"
        },
        dataType: "json",
        method: "POST",

        url: "/register/register",

        success: function (request){
            console.log("success")
        },

        error: function (request){
        console.log(request)
        }
    });

});
