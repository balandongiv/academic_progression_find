# profession.py

def prepare_sankey_data_profession(selected_professions, data):
    nodes = []
    links = []
    profession_index = {}
    subject_index = {}

    for subject in data['subjects']:
        for profession in subject['related_professions']:
            if profession in selected_professions:
                # Add professions to nodes if not already added
                if profession not in profession_index:
                    profession_index[profession] = len(nodes)
                    nodes.append({"name": profession})

                # Add subjects to nodes if not already added
                if subject['name'] not in subject_index:
                    subject_index[subject['name']] = len(nodes)
                    nodes.append({"name": subject['name']})

                # Create a link from profession to subject
                links.append({
                    "source": profession_index[profession],
                    "target": subject_index[subject['name']],
                    "value": 1
                })

    return nodes, links


import plotly.graph_objects as go

def prepare_sankey_data_subject_to_career(data, selected_subjects=None):
    nodes = []
    links = []
    subject_index = {}
    profession_index = {}

    subject_to_semester = {subject['name']: subject['semester'] for subject in data['subjects']}
    sbj_sem_list = []

    for subject in selected_subjects:
        sbj_sem = f"Semester {subject_to_semester[subject]}: {subject}"
        sbj_sem_list.append(sbj_sem)


    # sbj_sem=['tt','xxxx']
    for subject in data['subjects']:
        subject_name = subject['name']

        # Filter subjects based on selected_subjects
        if selected_subjects and subject_name not in selected_subjects:
            continue

        # Add subject to nodes if not already added
        if subject_name not in subject_index:
            subject_index[subject_name] = len(nodes)
            nodes.append({"name": subject_name})

        for profession in subject['related_professions']:
            # Add profession to nodes if not already added
            if profession not in profession_index:
                profession_index[profession] = len(nodes)
                nodes.append({"name": profession})

            # Create a link from subject to profession
            links.append({
                "source": subject_index[subject_name],
                "target": profession_index[profession],
                "value": 1
            })

    return nodes, links,sbj_sem_list


def generate_sankey_figure_profession(nodes, links, x_positions=None, y_positions=None, color='blue'):
    # Extracting sources, targets, and values from links
    sources = [link['source'] for link in links]
    targets = [link['target'] for link in links]
    values = [link['value'] for link in links]

    # Define the Sankey diagram
    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=[node['name'] for node in nodes],
            color=color
        ),
        link=dict(
            source=sources,  # The source indices
            target=targets,  # The target indices
            value=values     # The values (flow quantity)
        )
    )])

    fig.update_layout(title_text="Sankey Diagram", font_size=10)
    return fig