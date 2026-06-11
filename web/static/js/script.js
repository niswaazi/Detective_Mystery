function loginPlayer(){

    let username =
    document.getElementById(
        "username"
    ).value;

    if(username===""){
        alert("Masukkan nama");
        return;
    }

    document.getElementById(
        "hiddenUser"
    ).value = username;

    fetch("/login",{

        method:"POST",

        headers:{
            "Content-Type":
            "application/x-www-form-urlencoded"
        },

        body:
        "username="+username

    });

}

function sendMessage(){

    let username =
    document.getElementById(
        "username"
    ).value;

    let message =
    document.getElementById(
        "message"
    ).value;

    if(message===""){
        return;
    }

    fetch("/chat",{

        method:"POST",

        headers:{
            "Content-Type":
            "application/json"
        },

        body:JSON.stringify({

            username:username,
            message:message

        })

    });

    document.getElementById(
        "message"
    ).value="";

}

function loadMessages(){

    fetch("/messages")

    .then(r=>r.json())

    .then(data=>{

        let box =
        document.getElementById(
            "chat-box"
        );

        box.innerHTML="";

        data.forEach(msg=>{

            box.innerHTML +=
            "<p>"+msg+"</p>";

        });

        box.scrollTop =
        box.scrollHeight;

    });

}

function investigateLocation(){

    let username =
    document.getElementById(
        "username"
    ).value;

    let location =
    document.getElementById(
        "location"
    ).value;

    fetch("/investigate",{

        method:"POST",

        headers:{
            "Content-Type":
            "application/json"
        },

        body:JSON.stringify({

            username:username,
            location:location

        })

    })

    .then(r=>r.json())

    .then(data=>{

        document.getElementById(
            "clue-box"
        ).innerHTML =
        data.clue;

        loadNotes();
        loadScore();

    });

}

function loadNotes(){

    let username =
    document.getElementById(
        "username"
    ).value;

    fetch(
        "/notes?username="+
        username
    )

    .then(r=>r.json())

    .then(data=>{

        document.getElementById(
            "inventory"
        ).innerHTML =
        "<pre>"+data.notes+"</pre>";

    });

}

function loadScore(){

    let username =
    document.getElementById(
        "username"
    ).value;

    fetch(
        "/score?username="+
        username
    )

    .then(r=>r.json())

    .then(data=>{

        document.getElementById(
            "score"
        ).innerHTML =
        data.score;

    });

}

function checkGameStatus(){

    fetch("/game_status")

    .then(r => r.json())

    .then(data => {

        if(data.solved){

            let banner =
            document.getElementById(
                "winner-banner"
            );

            banner.style.display =
            "block";

            banner.innerHTML =

            "🏆 CASE SOLVED!<br><br>" +

            data.winner +

            " berhasil memecahkan kasus!" +

            "<br><br>" +

            "<pre>" +

            data.result +

            "</pre>";
        }

    });

}

setInterval(loadMessages,1000);

setInterval(loadScore,2000);

setInterval(checkGameStatus,1000);

loadMessages();

checkGameStatus();