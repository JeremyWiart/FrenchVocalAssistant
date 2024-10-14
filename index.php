<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Vocal Assitant</title>
    <script src="js/switch.js" defer></script>
    <script src="js/load.js" defer></script>
    <!--<script src="https://cdn.tailwindcss.com"></script> -->
    <link  rel="stylesheet" href="index_css.css" />
    <link  rel="stylesheet" href="https://cdn.jsdelivr.net/npm/tailwindcss@2.0.1/dist/tailwind.min.css" />
</head>

<body class="bg-gray-100">
    

    <main class="flex items-center justify-center p-32">
        <div class="bg-white shadow-md rounded-lg w-full max-w-lg">

            <div class="flex justify-around flex-wrap bg-gray-200 p-4 rounded-t-lg">
                <button id="login-btn" class="text-blue-500 font-semibold">Connexion</button>
                <button id="register-btn" class="text-gray-500">Registration</button>
            </div>

            
            <section id="login-section" class="p-6">
                <h2 class="text-2xl font-bold text-center mb-4">Connexion</h2>
                <form action="#" method="POST">
         
                    <div class="mb-4">
                        <label for="username" class="block text-gray-700">Username</label>
                        <input type="text" id="username" name="username"
                            class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring focus:border-blue-500"
                            required>
                    </div>
                  
                    <div class="mb-4">
                        <label for="login-password" class="block text-gray-700">Password</label>
                        <input type="password" id="login-password" name="password"
                            class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring focus:border-blue-500"
                            required>
                    </div>
                    
                    <div class="mb-4">
                        <button name="login" type="submit"
                            class="w-full bg-blue-500 text-white py-2 px-4 rounded-md hover:bg-blue-600">Connexion</button>
                    </div>
                  
                    <div class="text-center">
                        <a href="#" class="text-blue-500 hover:underline">Forget Password ?</a>
                    </div>
                </form>
            </section>
            <?php
            if (isset($_POST['login'])) {
                $username = htmlspecialchars(trim($_POST['username']));
                $password = htmlspecialchars(trim($_POST['password']));
                if (!empty($_POST['username']) and !empty($_POST['password'])) {
                    $password = sha1($_POST['password']);
                    require('conf/cfg.php');
                    $req = $connexion->prepare("SELECT * FROM user WHERE username=:username AND password=:password");
                    $req->bindValue(':username', $username, PDO::PARAM_STR);
                    $req->bindValue(':password', $password, PDO::PARAM_STR);
                    $req->execute();
                    $rows = $req->rowCount();
                    if ($rows == 1) {
                        session_start();
                        $_SESSION['username'] = $username;

                        header("location:http://localhost/home/");
                        ob_end_flush();

                    } else
                        echo "<div class=\"erreur\">Pseudo ou password incorrect </div>";
                } else
                    echo "<div class=\"erreur\">Veuillez remplire tous les champs </div>";
            }

            ?>

            <section id="register-section" class="p-6 hidden">
                <h2 class="text-2xl font-bold text-center mb-4">Registration</h2>
                <form action="#" method="POST">
                   
                    <div class="mb-4">
                        <label for="register-name" class="block text-gray-700">Username</label>
                        <input type="text" id="register-name" name="name"
                            class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring focus:border-blue-500"
                            required>
                    </div>
                   
                    <div class="mb-4">
                        <label for="register-email" class="block text-gray-700">Adresse e-mail</label>
                        <input type="email" id="register-email" name="email"
                            class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring focus:border-blue-500"
                            required>
                    </div>
                  
                    <div class="mb-4">
                        <label for="register-password" class="block text-gray-700">Mot de passe</label>
                        <input type="password" id="register-password" name="password"
                            class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring focus:border-blue-500"
                            required>
                    </div>
                  
                    <div class="mb-4">
                        <label for="confirm-password" class="block text-gray-700">Confirmer le mot de passe</label>
                        <input type="password" id="confirm-password" name="confirm_password"
                            class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring focus:border-blue-500"
                            required>
                    </div>
                  
                    <div class="mb-4">
                        <button type="submit"
                            class="w-full bg-green-500 text-white py-2 px-4 rounded-md hover:bg-green-600">S'inscrire</button>
                    </div>
                </form>
            </section>
        </div>
    </main>
</body>

</html>