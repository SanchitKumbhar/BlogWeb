// like and dislike 
function asyncLike(blogid, CSRFToken, counter) {

    let likeobj = document.querySelector(`.like-${counter}`);
    console.log((likeobj.innerHTML));
    if (likeobj.innerHTML == '<i class="fa-regular fa-heart"></i>') {
        likeobj.innerHTML = '<i class="fa-solid fa-heart"></i>';
    } else {
        likeobj.innerHTML = '<i class="fa-regular fa-heart"></i>';
    }

}
function asyncDisLike(blogid, CSRFToken, counter) {
    let dislikeobj = document.querySelector(`.dislike-${counter}`)
    dislikeobj.innerHTML = '<i class="fa-regular fa-heart"></i>';
    const data = {
        'blogid': blogid
    };
    let p = fetch("/dislike", {
        'method': 'POST',
        headers: {
            'Content-Type': 'application/json', // Set the content type to JSON
            'X-CSRFToken': CSRFToken // Include the CSRF token
        },
        body: JSON.stringify(data) // Convert the JavaScript object to a JSON string
    })
        .then(response => {
            // Check if the response is OK (status in the range 200-299)
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json(); // Parse the JSON from the response
        })
        .then(data => {
            // Handle the data from the response
            console.log('Success:', data);
        })
        .catch(error => {
            // Handle any errors that occurred during the fetch
            console.error('Error:', error);
        });
}


// comment
function comment(blogid, CSRFToken) {
    text = prompt("Enter your comment: ");
    data = {
        'text': text,
        'blogid': blogid,
    }
    let p = fetch("/comment", {
        'method': 'POST',
        headers: {
            'Content-Type': 'application/json', // Set the content type to JSON
            'X-CSRFToken': CSRFToken // Include the CSRF token
        },
        body: JSON.stringify(data) // Convert the JavaScript object to a JSON string

    })
        .then(response => {
            // Check if the response is OK (status in the range 200-299)
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json(); // Parse the JSON from the response
        })
        .then(data => {
            // Handle the data from the response
            console.log('Success:', data);
        })
        .catch(error => {
            // Handle any errors that occurred during the fetch
            console.error('Error:', error);
        });

}

// change profile

