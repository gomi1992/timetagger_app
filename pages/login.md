# Login

<script src='./app/tools.js'></script>

<script>
async function login() {

    let el = document.getElementById("result");
    
    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;
    let totp = document.getElementById("totp").value;

    let url = tools.build_api_url("webtoken_for_localhost")+"?username="+username+"&password="+password+"&totp="+totp;
    let init = {method: "GET", headers:{}};
    let res = await fetch(url, init);

    if (res.status != 200) {
        let text = await res.text();
        el.innerText = "Could not get token: " + text;
        el.innerHTML = el.innerHTML + "<br><a href='../'>TimeTagger home</a>";
        return;
    }

    let token = JSON.parse(await res.text()).token;
    tools.set_auth_info_from_token(token);
    el.innerText = "Token exchange succesful";

    let state = tools.url2dict(location.hash);
    location.replace(state.page || "./app/");
}

//window.addEventListener('load', login);
</script>
<form>
<div><a>username:</a><input id="username"></input></div>
<div><a>password:</a><input id="password" type="password"></input></div>
<div><a>totp:</a><input id="totp"></input></div>
<button class='whitebutton' onclick="login()">Login</button>
</form>
Logging in ...

<p id='result'></p>
