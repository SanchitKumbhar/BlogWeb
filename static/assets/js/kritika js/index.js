// let viewCount = 0;

// const eachBlog = document.querySelectorAll(".blog-post");


// eachBlog.forEach((eachBlog) => {

//     const viewCountDiv = document.querySelector(".view-blog-btn");
//     const viewCountPara = document.querySelector(".view-count");

//     viewCountDiv.addEventListener("click", () => {
//         viewCount= viewCount+1;
//         console.log("1 view", viewCount);


//         viewCountPara.innerHTML = viewCount;
//     });
// });

const burger = document.querySelector('.burger');
const navList = document.querySelector('.off-screen-menu');

burger.addEventListener('click', () => {
    burger.classList.toggle('active');
    navList.classList.toggle('active');
})