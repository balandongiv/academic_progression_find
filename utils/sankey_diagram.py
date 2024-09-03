import random
from collections import defaultdict

import plotly.graph_objects as go


# Function to generate random color
def random_color():
    return f'rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})'
# Define the find_related_subjects function here for completeness
def find_related_subjects(selected_subject, data):
    related_subjects = set()

    # First, find the prerequisites for the selected subject
    for subject in data['subjects']:
        if subject['name'] == selected_subject:
            prerequisites = {prerequisite['subject'] for prerequisite in subject.get('pre_requisites', [])}
            related_subjects.update(prerequisites)
            break

    # Then, find all subjects for which the selected subject is a prerequisite
    for subject in data['subjects']:
        for prerequisite in subject.get('pre_requisites', []):
            if prerequisite['subject'] == selected_subject:
                related_subjects.add(subject['name'])

    return list(related_subjects)


def generate_expected_semester_positions(selected_subject,data):
    subject_to_semester = {subject['name']: subject['semester'] for subject in data['subjects']}
    semester_positions = {}

    all_related_subjects = find_related_subjects(selected_subject,data)

    # Filter out subjects that do not exist in subject_to_semester to avoid KeyError
    valid_related_subjects = [subj for subj in all_related_subjects if subj in subject_to_semester]

    unique_semesters = sorted(set(subject_to_semester[subj] for subj in valid_related_subjects))
    for idx, sem in enumerate(unique_semesters):
        semester_positions[sem] = idx / max(1, len(unique_semesters) - 1)

    return semester_positions,all_related_subjects


def prepare_sankey_data_subject(selected_subject, data):
    nodes = []
    links = {'source': [], 'target': [], 'value': [], 'color': []}
    node_indices = {}
    x_positions = []
    y_positions = []


    semester_positions,all_related_subjects=generate_expected_semester_positions(selected_subject,data)

    subject_to_semester = {subject['name']: subject['semester'] for subject in data['subjects']}
    sbj_sem=f"Semester {subject_to_semester[selected_subject]}: {selected_subject}"
    # Set x positions dynamically based on semester
    unique_semesters = sorted(set(subject_to_semester[subj] for subj in all_related_subjects))
    for idx, sem in enumerate(unique_semesters):
        semester_positions[sem] = idx / max(1, len(unique_semesters) - 1)

        # Create nodes and links based on dependencies and successors
    y_offset = 0  # Start y position at the top
    y_spacing = 1.0 / max(1, len(all_related_subjects))
    # Organize subjects by semester


    for subject_name in all_related_subjects:
        current_node_label = f"Semester {subject_to_semester[subject_name]}: {subject_name}"

        if current_node_label not in node_indices:
            node_indices[current_node_label] = len(nodes)
            nodes.append(current_node_label)
            x_positions.append(semester_positions[subject_to_semester[subject_name]])  # Assign x based on semester
            y_positions.append(y_offset)
            y_offset += y_spacing

    # Create links based on dependencies and successors
    for subject in data['subjects']:
        if subject['name'] not in all_related_subjects:
            continue

        current_node_label = f"Semester {subject_to_semester[subject['name']]}: {subject['name']}"

        # Add links for prerequisites
        for prereq in subject.get('pre_requisites', []):
            prereq_name = prereq['subject']
            prereq_label = f"Semester {subject_to_semester[prereq_name]}: {prereq_name}"
            if prereq_label in node_indices and current_node_label in node_indices:
                links['source'].append(node_indices[prereq_label])
                links['target'].append(node_indices[current_node_label])
                links['value'].append(1)  # Set link weight

                # Assign random color for each path
                links['color'].append(random_color())

    return nodes, links, x_positions, y_positions,sbj_sem



def prepare_sankey_data_semester_progression(selected_semesters, selected_subjects, data, highlight_subjects):
    nodes = []
    links = {'source': [], 'target': [], 'value': [], 'color': []}
    node_indices = {}
    x_positions = []
    y_positions = []

    # Organize subjects by semester
    semester_to_subjects = defaultdict(list)
    for subject in data['subjects']:
        semester_to_subjects[subject['semester']].append(subject)

    # Calculate x positions for each semester
    semester_count = len(selected_semesters)
    semester_positions = {sem: i / max(1, semester_count - 1) for i, sem in enumerate(sorted(selected_semesters))}

    # Set y positions dynamically
    y_spacing = 1.0 / max(len(semester_to_subjects[sem]) for sem in selected_semesters) if selected_semesters else 0.1

    # Create nodes and set x and y positions for each semester
    for semester in sorted(semester_to_subjects.keys()):
        if selected_semesters and semester not in selected_semesters:
            continue

        subjects = semester_to_subjects[semester]
        y_offset = 0  # Start y position at the top

        for subject in subjects:
            subject_name = subject['name']
            current_node_label = f"Semester {semester}: {subject_name}"

            # Filter based on selected subjects
            if selected_subjects and subject_name not in selected_subjects:
                continue

            # Add current subject node if not present
            if current_node_label not in node_indices:
                node_indices[current_node_label] = len(nodes)
                nodes.append(current_node_label)
                x_positions.append(semester_positions[semester])  # Assign x position based on semester
                y_positions.append(y_offset)  # Assign y position
                y_offset += y_spacing  # Increment y position for next node

    # Create links based on prerequisites
    for semester in sorted(semester_to_subjects.keys()):
        if selected_semesters and semester not in selected_semesters:
            continue

        subjects = semester_to_subjects[semester]
        for subject in subjects:
            current_node_label = f"Semester {semester}: {subject['name']}"

            # Filter based on selected subjects
            if selected_subjects and subject['name'] not in selected_subjects:
                continue

            # Add links based on actual prerequisites
            for prereq in subject.get('pre_requisites', []):
                prereq_name = prereq['subject']

                # Find the correct semester for the prerequisite
                for prev_sem in range(1, semester):
                    if any(prereq_name == s['name'] for s in semester_to_subjects[prev_sem]):
                        prereq_node_label = f"Semester {prev_sem}: {prereq_name}"

                        if prereq_node_label in node_indices:
                            # Add link from prerequisite to current subject
                            links['source'].append(node_indices[prereq_node_label])
                            links['target'].append(node_indices[current_node_label])
                            links['value'].append(1)  # Set link weight

                            # Assign random color for each path
                            links['color'].append(random_color())

                            break  # Only need to connect once

    return nodes, links, x_positions, y_positions

def generate_sankey_figure(nodes, links, x_positions=None, y_positions=None, color='blue'):
    # Extracting sources, targets, and values from links
    sources = links['source']
    targets = links['target']
    values = links['value']

    # Define the Sankey diagram
    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=nodes,
            color=color
        ),
        link=dict(
            source=sources,  # The source indices
            target=targets,  # The target indices
            value=values,    # The values (flow quantity)
            color=links['color']  # Optional: link colors
        )
    )])

    fig.update_layout(title_text="Sankey Diagram", font_size=10)
    return fig
