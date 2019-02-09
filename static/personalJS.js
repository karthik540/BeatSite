var botPart1 = '<div class="chat-container darker"><img src="../static/Assets/avatar.jpg" alt="Avatar" style="width:100%;"><p>';
var userPart1 = '<div class="chat-container"><img src="../static/Assets/userImage.png" alt="Avatar" style="width:100%;" class = "right"><p>'
var botPart3 ='</p></div>';
function toggleLoginModal()
{
    if($(".modal").css("display") == "none")
    {
        $(".modal").css("display", "block");
    }
    else
    {
        $(".modal").css("display", "none");
    }
}

//Bot Window pop up...
function openBotWindow()
{    
    $("#botWindow").css("display", "block");
    console.log("works !")
}

function closeBotWindow()
{
    $("#botWindow").css("display", "none");
}

//User Message Reciever...
function sendMessage()
{
    var utext = $("#msgBox").val();
    var flag = false;
    $(".chat-parent-container").append(userPart1 + utext + botPart3);
    $.ajax({
        type: "POST",
        url: "/botresponse",
        data: {'utext' : utext},
        success: function (response) {
            console.log(botPart1 + response + botPart3);
            $(".chat-parent-container").append(botPart1 + response + botPart3);
            flag = true;
        },
        error: function(){
            $(".chat-parent-container").append(botPart1 + "Sorry, Technical Issues !" + botPart3);
        },
        complete: function(){
            $("#msgBox").val('').empty();
        }
    });        
    
}


$(document).ready(function () {

//Responsive navbar...

$(".icon").click(function (e) {
    if($(".top-nav").hasClass(".responsive"))
    {
        $(".top-nav").removeClass(".responsive");

        console.log("response removed !");
    }
    else
    {
        $(".top-nav").addClass(".responsive");
        console.log("response added !");
    }
});


//Login and SignUp Modals...
//Signup Modal...

$("#signUpButton").click(function (e) {
    $(".modal").css("display", "block");
    $("#SignUpModal").css("z-index", "8");
    $("#LoginModal").css("z-index", "0");
    e.preventDefault();
});

//Login Modal...

$("#loginButton").click(function (e) {
    $(".modal").css("display", "block");
    $("#SignUpModal").css("z-index", "0");
    $("#LoginModal").css("z-index", "8");
    e.preventDefault();
});

$(".close").click(function (e) {
    $(".modal").css("display", "none");
    e.preventDefault();
});




});
