function addToFavourites() {
    {% if user.is_authenticated %}
        alert('Added to Favourites');
    {% else %}
        var loginMessage = document.getElementById("login-message");
        if (loginMessage) {
            loginMessage.style.display = "block";
        }
    {% endif %}
}
