let viewCount = 0;

// const viewCountDiv = document.querySelectorAll(".view-blog-btn");
// const viewCountPara = document.getElementById("#view-count");
const eachBlog = document.querySelectorAll(".blog-post");


eachBlog.forEach((eachBlog) => {
    // eachBlog.addEventListener("click", () => {
    const viewCountDiv = document.querySelector(".view-blog-btn");
    const viewCountPara = document.querySelector(".view-count");

    viewCountDiv.addEventListener("click", () => {
        viewCount= viewCount+1;
        console.log("1 view", viewCount);
        // changingViewCount(viewCountDiv);

        viewCountPara.innerHTML = viewCount;
    });
});

