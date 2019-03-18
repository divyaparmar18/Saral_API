const axios = require('axios');
const read = require('readline-sync');
var slug_list = [];
var course_list;

// main function to get the course_list
async function All_data(Exercise_data) {
    var url = "http://saral.navgurukul.org/api/courses"

//function in a function to get exercise_list
    async function Exercise_data(slug_data) {
        for (i = 0; i < course_list.length; i++) {
            var course = course_list[select_course - 1]
}
            const newurl = url + "/" + course + "/exercises"

//function inside function to get slug_data
        async function slug_data(further_process) {
            select_exercise = read.question("enter exercise and for 'courses back' put 'up'")
            if (select_exercise == 'up') {
                (All_data());
                return

            }
            else if (select_exercise <= slug_list.length) {
                for (i = 0; i < slug_list.length; i++) {
                    var currentIndex = [select_exercise - 1]
                    var slug = slug_list[currentIndex]
                }
                var another_url = "http://saral.navgurukul.org/api/courses/75/exercise/getBySlug?slug=" + slug
            }
            else {
                console.log("Invalid input")
            }
//function in function for further process        
    async function further_process() {
         while (true) {
            var what_next = read.question("what you want? for previous press 'p' for next press 'n'  for 'exercises' press 'upp' and to exit press 'exit'")
            if (what_next == 'upp') {
                (Exercise_data());
                return
        }
        else if (what_next === 'p' && currentIndex >= 0 && currentIndex < slug_list.length) {
            currentIndex = currentIndex - 1
                if (currentIndex <= 0) {
                    console.log("No pages, this is the last page")
            }
                else {
                current = slug_list[currentIndex]
                another_url = "http://saral.navgurukul.org/api/courses/75/exercise/getBySlug?slug=" + current
                    await axios.get(another_url).then(respond => {
                        const content = respond.data.content
                        console.log(content)
                        return
                }).then()
            }
        }
            else if (what_next === 'n' && currentIndex < slug_list.length) {
                currentIndex++
                if (currentIndex == slug_list.length) {
                    console.log("No pages, this is the last page")
    }
                else {
                current = slug_list[currentIndex]
                    console.log(current)
                    another_url = "http://saral.navgurukul.org/api/courses/75/exercise/getBySlug?slug=" + current
                        await axios.get(another_url).then(respond => {
                        const content = respond.data.content
                        console.log(content)
                        return
                }).then()
            }
            }
                else if (what_next === 'exit') {
                break
        }
                else {
                console.log("There is an error input is not valid")
        }
    }
}
            axios.get(another_url).then(respond => {
            const content = respond.data.content
            console.log(content)
            further_process();
    })
}
        await axios.get(newurl).then(respo => {
            slug_list = []
            var count = 1
            const allExercise = respo.data.data;
            for (i = 0; i < allExercise.length; i++) {
                let exercise = allExercise[i];
                console.log(count, "Exercise Name", exercise.name);
                count++
                slug_list.push(exercise.slug);
                //console.log(slug_list)
                const child_exercise = exercise.childExercises
                for (j = 0; j < child_exercise.length; j++) {
                    console.log(count, "     Child exercise name      ", child_exercise[j].name)
                    slug_list.push(child_exercise[j].slug)
                    count++
                }
            }
            (slug_data());
        })
    }
    await axios.get(url).then(response => {
        //availableCourses contains list of courses
        const availableCourses = response.data.availableCourses;
        course_list = []
        count = 1
        for (i = 0; i < availableCourses.length; i++) {
            let course = availableCourses[i];
            console.log("----------------");
            console.log(count + " :- courses NAme :- ", course.name);
            count++
            console.log("The Id is", course.id)
            course_list.push(course.id)
        }
        select_course = read.question("enter the course")
        if (select_course <= course_list.length) {
            Exercise_data();
        }
        else {
            console.log("invaid input")
        }
    })
}
All_data();
/*
slugs = []

currentIndex = 5

//  previous
currentIndex = currentIndex - 1 // 4
currentSlug = slugs[currentIndex]


currentIndex = currentIndex + 1 // 5
currentSlug = slugs[currentIndex]
*/