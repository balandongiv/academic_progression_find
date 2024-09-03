The idea was to show the academic progression semester by semester using sankey graph. 
To have interactive interface, we will use streamlit.
Which consist of multiple tabs, where the first tab show subjects to career prospects, 
the second tab show semester progression, 
and the third tab customizable view.

There is also option to filter by only one or multiple using feature
selected_semesters = st.multiselect("Filter by Semester", semesters)
selected_professions = st.multiselect("Filter by Profession", professions)
selected_plos = st.multiselect("Filter by Program Learning Outcome", plos)

When filtering, the sankey graph will be updated accordingly.
Also, when filtering by profession or PLO, the visualization is from left to right, where,
the left side is the first semester, followed by the second semester and so on. This to show the progression of the subjects by semester.


Sankey diagram to flow horizontally from left to right, with each semester represented as a column, and the subjects for each semester listed under their respective columns.

```python

Thank you for providing the image. It clarifies that you want a straightforward tabular or columnar representation of subjects listed under their respective semesters, arranged horizontally from left to right.

Let's update the Streamlit application to reflect this specific visual requirement, focusing on creating a view where each semester and its subjects are clearly displayed in columns.

Streamlit App for Semester-wise Subject Display
We'll create a Streamlit app that presents subjects under each semester in a horizontal layout, similar to the table-like structure shown in the image.



Thank you for the clarification. You would like the correct visual layout as shown in the image with a columnar representation of semesters and subjects, along with an interactive Sankey diagram that updates based on selected filters. This means integrating both a tabular view and a Sankey diagram into the Streamlit app.



for each subject, add extra detail
- The first detail, pre-requisite subjects that is needed when taking the subject, this is only applicable for subject in semester  2 and above. Assume, in actual situation, some subject may not have any pre requisite, have only one, or perhaps, more than 3 pre-requiste. Give also the value in hourly, from one hour to maximum 120 hours student learning time that lead to the pre-requisite.

- The second detail are, profession that is related when taking the subject, it can be no profession, one profession or more than one profession

streamlit run app.py

Plan to Fix the Representation Issue
Always Display Subjects Under Their Respective Semester: Ensure that subjects are correctly placed in their respective semester columns, regardless of prerequisite or successor relationships.
Ensure that subjects appear under their respective semesters: Subjects should not shift to different semester columns if their prerequisite or successor subjects are filtered out.


Handle Disconnected Nodes: Even if a subject doesn't have prerequisites or isn't a prerequisite for another subject in the selected semesters, it should still appear in its correct semester column.

Filter Adjustment: Adjust how subjects are shown when filtering to make sure that every selected semester has its corresponding subjects displayed in the Sankey diagram correctly.
Avoid displaying nodes in the wrong semester columns: When filtering by semesters, ensure that subjects without connections still appear correctly under their respective semester columns.



To implement the functionality in Tab 4 where selecting a specific subject displays all its dependencies (prerequisites) and subjects that are dependent on it (successors), we need to dynamically trace both backward and forward relationships from the selected subject. This feature will provide a focused view of the academic progression related to a single subject.



- The third section is program learning outcome that is related to each subject. each subject  have 3 specific PLO assign to them. there are in total 11 PLO which are
1)  knowledge and understanding
2) Cognitive skills
3) Practical Skills
4) Interpersonal Skills
5) Communication Skills
6) Digital Skills
7) Numeracy Skills
8) Leadership, autonomy and responsibility
9) Personal Skills
10) Entrepreneurial Skills
11) Ethics and Professionalism

Using you own intelligence, create a new json structure that can incorporate all this request for each subject,  



given the json as above, suggest a new streamlit that where, the first tab, show subjects to career prospects
the second tab show semester progression, you must make sure, the semester is sort from semester 1, semester 2 and so on
the third tab customizable view

maintain also the filter options, where use can filter by only one or multiple
-  semester,
- pre_requisites,
- professions
- program learning outcome

assume we simply import the json, therefore, do not show in the code . give no explanation but just the complete code


##################

Create a JSON structure for the provided physics subjects, incorporating the following information for each subject:

Name: The subject's full name.
Semester: The semester in which the subject is offered (as an integer).
Pre-requisites: A list of subject names that must be completed before taking this subject.
Related Professions: A list of professions related to the subject.
Program Learning Outcomes (PLOs): A list of PLOs associated with the subject, selected from the following options:
Knowledge and understanding
Cognitive skills
Practical Skills
Interpersonal Skills
Communication Skills
Digital Skills
Numeracy Skills
Leadership, autonomy, and responsibility
Personal Skills   
Entrepreneurial Skills
Ethics and Professionalism
Subject Data:

The provided list of physics subjects, including their names, nature, year, and semester.

{
  "subjects": [
    {"Subject": "Physics Mechanics", "Nature": "Program Core", "Nature in template": "Physics/ Fundamental Course", "Year": 1, "Sem": 1},
    {"Subject": "Experiment and Measurement Method for Physics", "Nature": "Program Core", "Nature in template": "Physics/ Fundamental Course", "Year": 1, "Sem": 1},
    {"Subject": "Physic Practical", "Nature": "Program Core", "Nature in template": "", "Year": 1, "Sem": 2},
    {"Subject": "Wave and Optics", "Nature": "Program Core", "Nature in template": "Physics/ Fundamental Course", "Year": 1, "Sem": 2},
    {"Subject": "Mathematical methods in Physics 1", "Nature": "Program Core", "Nature in template": "Physics/ Fundamental Course", "Year": 1, "Sem": 2},
    {"Subject": "Physical Practical 2", "Nature": "Program Core", "Nature in template": "", "Year": 2, "Sem": 3},
    {"Subject": "Modern Physics", "Nature": "Program Core", "Nature in template": "Physics/ Fundamental Course", "Year": 2, "Sem": 3},
    {"Subject": "Mathematical methods in Physic 2", "Nature": "Program Core", "Nature in template": "", "Year": 2, "Sem": 3},
    {"Subject": "Basic Electronic", "Nature": "Program Core", "Nature in template": "", "Year": 2, "Sem": 3},
    {"Subject": "Physics Practical 3", "Nature": "Program Core", "Nature in template": "", "Year": 2, "Sem": 4},
    {"Subject": "Electricity and magnetism", "Nature": "Program Core", "Nature in template": "", "Year": 2, "Sem": 4},
    {"Subject": "Quantum Physics", "Nature": "Program Core", "Nature in template": "Physics/ Fundamental Course", "Year": 2, "Sem": 4},
    {"Subject": "Thermodynamics Physics", "Nature": "Program Core", "Nature in template": "Physics/ Fundamental Course", "Year": 2, "Sem": 4},
    {"Subject": "Digital Electronics", "Nature": "Program Core", "Nature in template": "", "Year": 2, "Sem": 4},
    {"Subject": "Statistical Physics", "Nature": "Program Core", "Nature in template": "Physics/ Fundamental Course", "Year": 3, "Sem": 5},
    {"Subject": "Solid State Physics", "Nature": "Program Core", "Nature in template": "Physics/ Fundamental Course", "Year": 3, "Sem": 5},
    {"Subject": "Computational Physics and Modelling", "Nature": "Program Core", "Nature in template": "Physics/ Fundamental Course", "Year": 3, "Sem": 5},
    {"Subject": "Advanced Electronics", "Nature": "Program Core", "Nature in template": "", "Year": 3, "Sem": 5},
    {"Subject": "Optoelectronics", "Nature": "Program Core", "Nature in template": "", "Year": 3, "Sem": 5},
    {"Subject": "Scientific Project 1", "Nature": "Program Core", "Nature in template": "", "Year": 3, "Sem": 6},
    {"Subject": "Semiconductor Physics", "Nature": "Program Core", "Nature in template": "Physics/ Fundamental Course", "Year": 3, "Sem": 6},
    {"Subject": "Applied Physics In Industrial Design", "Nature": "Program Core", "Nature in template": "", "Year": 3, "Sem": 6},
    {"Subject": "Scientific Project 2", "Nature": "Program Core", "Nature in template": "", "Year": 3, "Sem": 7},
    {"Subject": "Instrumentation Physics", "Nature": "Program Core", "Nature in template": "", "Year": 3, "Sem": 7},
    {"Subject": "Noise and Vibration", "Nature": "Elective Course", "Nature in template": "Applied Course", "Year": 3, "Sem": 6},
    {"Subject": "X-Ray Crystallography", "Nature": "Elective Course", "Nature in template": "Applied Course", "Year": 3, "Sem": 6},
    {"Subject": "Nuclear Physic", "Nature": "Elective Course", "Nature in template": "Applied Course", "Year": 3, "Sem": 6},
    {"Subject": "Communication Electronic", "Nature": "Elective Course", "Nature in template": "Applied Course", "Year": 3, "Sem": 6},
    {"Subject": "Microcontroller", "Nature": "Elective Course", "Nature in template": "Applied Course", "Year": 3, "Sem": 6},
    {"Subject": "Digital Signal Processing", "Nature": "Elective Course", "Nature in template": "Applied Course", "Year": 3, "Sem": 6},
    {"Subject": "Computer Programming", "Nature": "Elective Course", "Nature in template": "Applied Course", "Year": 3, "Sem": 6},
    {"Subject": "Special Topic in Industrial Physics", "Nature": "Elective Course", "Nature in template": "Applied Course", "Year": 3, "Sem": 6},
    {"Subject": "Electroacoustic", "Nature": "Elective Course", "Nature in template": "Applied Course", "Year": 3, "Sem": 7},
    {"Subject": "Solar Energy Technology and System", "Nature": "Elective Course", "Nature in template": "Applied Course", "Year": 3, "Sem": 7},
    {"Subject": "Nanotechnology", "Nature": "Elective Course", "Nature in template": "Applied Course", "Year": 3, "Sem": 7},
    {"Subject": "Non-Destructive Testing", "Nature": "Elective Course", "Nature in template": "Applied Course", "Year": 3, "Sem": 7},
    {"Subject": "Introduction to Astronomy", "Nature": "Elective Course", "Nature in template": "Applied Course", "Year": 3, "Sem": 7},
    {"Subject": "Semiconductor Technology", "Nature": "Elective Course", "Nature in template": "Applied Course", "Year": 3, "Sem": 7},
    {"Subject": "Laser Physics", "Nature": "Elective Course", "Nature in template": "Applied Course", "Year": 3, "Sem": 7},
    {"Subject": "Logic and Problem Solving Design in Science and Technology", "Nature": "Faculty Core", "Nature in template": "Faculty Core", "Year": 1, "Sem": 1},
    {"Subject": "Basic Statistics", "Nature": "Faculty Core", "Nature in template": "Faculty Core", "Year": 1, "Sem": 2},
    {"Subject": "Basic Chemistry", "Nature": "Faculty Core", "Nature in template": "Faculty Core", "Year": 2, "Sem": 3},
    {"Subject": "Research Methodology and Scientific Writing", "Nature": "Faculty Core", "Nature in template": "Faculty Core", "Year": 2, "Sem": 4},
    {"Subject": "Data Analytics in Science and Technology", "Nature": "Faculty Core", "Nature in template": "Faculty Core", "Year": 2, "Sem": 4},
    {"Subject": "Earth Science", "Nature": "Faculty Core", "Nature in template": "Faculty Core", "Year": 3, "Sem": 5}
  ],
Additional Considerations:

PLO Mapping: Determine the most relevant PLOs for each subject based on its content and objectives.
Pre-requisite Information: If pre-requisites are not explicitly stated, consult course catalogs or subject outlines to identify them.
Related Professions: Research the career paths and industries commonly associated with each subject.
Example JSON Structure:

JSON
{
  "subjects": [
    {
      "name": "Physics Mechanics",
      "semester": 1,
      "pre-requisites": [],
      "related_professions": ["Physicist", "Engineer", "Scientist"],
      "program_learning_outcomes": [
        "Knowledge and understanding",
        "Cognitive skills",
        "Practical Skills"
      ]
    },
    // ... other subjects
  ]
}
