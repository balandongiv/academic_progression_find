import streamlit as st
from utils.data_loader import load_data
from utils.sankey_diagram import (
    prepare_sankey_data_semester_progression,
    prepare_sankey_data_subject,
    generate_sankey_figure
)
from utils.profession import (
    prepare_sankey_data_profession,
    generate_sankey_figure_profession,
    prepare_sankey_data_subject_to_career  # Import the new function
)

# streamlit run app.py
def main():
    # Load data
    data = load_data()

    # Streamlit app layout
    st.title("Academic Progression Visualization")

    # Tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Subjects to Career Prospects",
        "Semester Progression",
        "Customizable View",
        "Subject Dependency View",
        "Professions to Subjects"  # New tab for profession to subjects
    ])

    with tab1:
        st.subheader("Subjects to Career Prospects")

        # Get the list of all subjects from the data
        subjects = sorted({subject['name'] for subject in data['subjects']})

        # Multiselect for subjects with a unique key
        selected_subjects = st.multiselect("Filter by Subject", subjects, default=subjects, key="tab1_subjects")

        # Prepare Sankey Data for Subjects to Career Prospects based on selected subjects
        nodes, links,sbj_sem = prepare_sankey_data_subject_to_career(data, selected_subjects)

        # Debugging: Display nodes and links
        st.write(f"Selected subject: {sbj_sem}")
        st.write("Nodes:", nodes)
        st.write("Links:", links)

        # Check if the nodes and links are not empty
        if nodes and links:
            # Generate Sankey Diagram
            fig = generate_sankey_figure_profession(nodes, links, x_positions=[], y_positions=[], color='purple')
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("No data available to generate the diagram for the selected subjects.")

    with tab2:
        st.subheader("Semester Progression with Sankey Diagram")

        semesters = sorted({subject['semester'] for subject in data['subjects']})
        subjects = sorted({subject['name'] for subject in data['subjects']})

        selected_semesters = st.multiselect("Filter by Semester", semesters, default=semesters, key="tab2_semesters")
        selected_subjects = st.multiselect("Filter by Subject", subjects, default=subjects, key="tab2_subjects")
        highlight_subjects = st.multiselect("Highlight Paths for Subjects", subjects, key="tab2_highlight_subjects")

        # Prepare Sankey Data for Semester Progression
        nodes, links, x_positions, y_positions = prepare_sankey_data_semester_progression(
            selected_semesters, selected_subjects, data, highlight_subjects
        )

        # Generate Sankey Diagram
        fig = generate_sankey_figure(nodes, links, x_positions, y_positions, color='blue')
        st.plotly_chart(fig, use_container_width=True)

    with tab3:
        st.subheader("Customizable View - Coming Soon")

    with tab4:
        st.subheader("Subject Dependency View")

        # Get the list of subjects from the data
        subjects = sorted({subject['name'] for subject in data['subjects']})

        # Select subject with a unique key
        selected_subject = st.selectbox("Select a Subject", subjects, key="tab4_select_subject")



        # Check if the selected_subject is not None or empty
        if selected_subject:
            # Prepare Sankey Data for the selected subject
            nodes, links, x_positions, y_positions,selected_subject_sem = prepare_sankey_data_subject(selected_subject, data)
            # Debugging: Display selected subject
            st.write(f"Selected subject: {selected_subject_sem}")
            # Debugging: Display nodes and links
            print(f"this is nodes {nodes}")
            sorted_nodes = sorted(nodes, key=lambda x: int(x.split()[1].rstrip(':')))
            st.write("Nodes:", sorted_nodes)
            # st.write("Links:", links)

            # Check if the nodes and links are not empty
            if nodes and links:
                # Generate Sankey Diagram
                fig = generate_sankey_figure(nodes, links, x_positions, y_positions, color='green')
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.warning("No data available to generate the diagram for the selected subject.")
        else:
            st.warning("Please select a subject to view its dependency.")

    with tab5:
        st.subheader("Professions to Subjects")

        # Get the list of all professions from the data
        professions = sorted(set(prof for subject in data['subjects'] for prof in subject['related_professions']))

        # Multiselect for professions with a unique key
        selected_professions = st.multiselect("Select Professions", professions, default=professions, key="tab5_professions")

        # Check if there are selected professions
        if selected_professions:
            # Prepare Sankey Data for the selected professions
            nodes, links = prepare_sankey_data_profession(selected_professions, data)
            # Debugging: Display nodes and links
            st.write("Nodes:", nodes)
            st.write("Links:", links)
            # Check if the nodes and links are not empty
            if nodes and links:
                # Generate Sankey Diagram
                fig = generate_sankey_figure_profession(nodes, links, x_positions=[], y_positions=[], color='orange')
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.warning("No data available to generate the diagram for the selected professions.")
        else:
            st.warning("Please select at least one profession to view related subjects.")

if __name__ == "__main__":
    main()
