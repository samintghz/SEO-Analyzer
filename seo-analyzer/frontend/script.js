async function analyze() {


    const url = document.getElementById("urlInput").value;


    if (!url) {

        alert("Please enter a website URL");
        return;

    }



    // Show loading

    document
    .getElementById("loading")
    .classList
    .remove("hidden");



    document
    .getElementById("result")
    .classList
    .add("hidden");





    try {


        const response = await fetch(
            "http://127.0.0.1:8000/analyze",
            {

                method: "POST",

                headers: {

                    "Content-Type": "application/json"

                },

                body: JSON.stringify({

                    url: url

                })

            }

        );



        const data = await response.json();



        console.log(data);





        // Hide loading

        document
        .getElementById("loading")
        .classList
        .add("hidden");



        // Show result

        document
        .getElementById("result")
        .classList
        .remove("hidden");







        // SEO Score


        document
        .getElementById("scoreValue")
        .innerText = data.seo_score;




        // Change circle color


        const circle = document.querySelector(".circle");



        if (data.seo_score >= 80) {


            circle.style.borderColor = "green";


        } 
        else if (data.seo_score >= 50) {


            circle.style.borderColor = "orange";


        } 
        else {


            circle.style.borderColor = "red";


        }








        // Categories


        const categories = data.analysis.categories;






        // Technical SEO


        document
        .getElementById("technicalScore")
        .innerText =
        categories.technical_seo + "/60";



        document
        .getElementById("technicalBar")
        .style.width =
        (categories.technical_seo / 60 * 100) + "%";








        // Performance


        document
        .getElementById("performanceScore")
        .innerText =
        categories.performance + "/20";



        document
        .getElementById("performanceBar")
        .style.width =
        (categories.performance / 20 * 100) + "%";








        // Accessibility


        document
        .getElementById("accessibilityScore")
        .innerText =
        categories.accessibility + "/20";



        document
        .getElementById("accessibilityBar")
        .style.width =
        (categories.accessibility / 20 * 100) + "%";








        // Content SEO


        document
        .getElementById("contentScore")
        .innerText =
        categories.content_seo + "/40";



        document
        .getElementById("contentBar")
        .style.width =
        (categories.content_seo / 40 * 100) + "%";









        // Website Information



        document
        .getElementById("siteTitle")
        .innerText =
        data.analysis.title || "No title";




        document
        .getElementById("siteDescription")
        .innerText =
        data.analysis.description || "No description";




        document
        .getElementById("loadTime")
        .innerText =
        data.analysis.load_time;




        document
        .getElementById("totalLinks")
        .innerText =
        data.analysis.links_analysis?.total_links || 0;




        document
        .getElementById("brokenLinks")
        .innerText =
        data.analysis.links_analysis?.broken_links || 0;









        // Recommendations


        const list =
        document.getElementById(
            "recommendationList"
        );



        list.innerHTML = "";



        if(data.recommendations.length === 0){


            const li = document.createElement("li");

            li.innerText = "Great! No major SEO issues found.";

            list.appendChild(li);


        }

        else {


            data.recommendations.forEach(item => {


                const li =
                document.createElement("li");



                li.innerText = item;



                list.appendChild(li);


            });


        }




    }



    catch(error){



        console.log(error);



        document
        .getElementById("loading")
        .classList
        .add("hidden");



        alert(
            "Something went wrong"
        );

    }


}