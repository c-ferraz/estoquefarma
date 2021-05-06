//  var botao = document.getElementById("buconteudoon1");
//  botao.addEventListener('click', function() {
//                                      login();
//                                  });
// function ValidarAcesso(){
// var nome="useradm";
// var senha="123456";
// var ninput=document.getElementById("input1");
// var sinput=document.getElementById("input2");
// if (nome === ninput && senha === sinput){
    

// }


// }

var usuarios = [
    {"login": "useradm", "senha": "123456"},
    {"login": "test", "senha": "test"},
    {"login": "estoquefarma", "senha": "estoquefarma"},
];

function login() {
    var usuario = document.getElementsByName('usuario')[0].value.toLowerCase();
    var senha = document.getElementsByName('senha')[0].value;
    

    for (var u in usuarios) {
        var us = usuarios[u];
        if (us.login === usuario && us.senha === senha) {
            window.location = "inicial.html";
            return true;
        }
    }
        
    alert("Dados incorretos, tente novamente.");
    window.location = "index.html";
    return false;
        
}

function cadastrar(){
    location.href='cadastro';
}

function alocar(){
    location.href='alocar';
}

function desalocar(){
    location.href='desalocar';
}

function atualizar(){
    location.href='atualizar';
}

function consultar(){
    location.href='consultar';
}

function menuPrincipal(){
    const menu_principal = document.getElementById('menu_principal');
    menu_principal.style.display='block';
    menu_principal.innerHTML=`
    <h1 class="top">ESTOQUEFARMA +</h1>
    <nav class="navbar">
        <button class="button" onclick="cadastrar()" style="vertical-align:middle" ><span> Cadastrar  </span></button>
        <button class="button" onclick="alocar()" style="vertical-align:middle" ><span> Alocar</span></button>
        <button class="button" onclick="desalocar()" style="vertical-align:middle" ><span> Desalocar</span></button>
        <button class="button" onclick="consultar()" style="vertical-align:middle" ><span>Consultar</span></button>
        <button class="button" onclick="consultar()" style="vertical-align:middle" ><span>Atualizar </span></button>
    </nav>
    `;
}
/* #conteudo{
  background-color: chartreuse;
  width: 500px;
  height: 700px;mn,
} */