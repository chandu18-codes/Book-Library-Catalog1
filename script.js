const searchBox = document.getElementById("searchBox");
const books = document.querySelectorAll(".book");

searchBox.addEventListener("input", function () {

    const searchText = searchBox.value.toLowerCase();

    books.forEach(function (book) {

        const bookText = book.textContent.toLowerCase();

        if (bookText.includes(searchText)) {
            book.style.display = "block";
        } else {
            book.style.display = "none";
        }

    });

});
