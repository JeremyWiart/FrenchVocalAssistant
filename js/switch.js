// Gestion de l'affichage entre Connexion et Inscription
const loginBtn = document.getElementById('login-btn');
const registerBtn = document.getElementById('register-btn');
const loginSection = document.getElementById('login-section');
const registerSection = document.getElementById('register-section');

loginBtn.addEventListener('click', () => {
    loginSection.classList.remove('hidden');
    registerSection.classList.add('hidden');
    loginBtn.classList.add('text-blue-500');
    loginBtn.classList.remove('text-gray-500');
    registerBtn.classList.add('text-gray-500');
    registerBtn.classList.remove('text-blue-500');
});

registerBtn.addEventListener('click', () => {
    registerSection.classList.remove('hidden');
    loginSection.classList.add('hidden');
    registerBtn.classList.add('text-blue-500');
    registerBtn.classList.remove('text-gray-500');
    loginBtn.classList.add('text-gray-500');
    loginBtn.classList.remove('text-blue-500');
});