import pandas as pd

side_info = pd.read_csv("../data/processed/side_info.csv", index_col=0)


def get_description(feature, abbreviation):
    """Gets the description of the abbreviation, or value, of a given feature
    based on the descriptions in the side info data frame.

    Args:   feature (string)
            abbreviation (char)

    Return: description of the feature value (string)
    """
    # get description from the side info data frame
    info_id = side_info[side_info["name"] == feature].index[0]
    description = side_info.loc[info_id, "description"]
    description_list = description.split(",")

    # go looking for the given abbreviation
    for des in description_list:
        feat_descr, feat_abbr = des.split("=")
        feat_descr = feat_descr.lstrip()
        feat_abbr = feat_abbr.lstrip()

        # if found, return description
        if feat_abbr == abbreviation:
            return feat_descr

    # if the abbreviation was not found,
    # print warning message and return abbreviation
    print("No description found in feature: " + feature + " for " + abbreviation)
    return abbreviation


def automated_questions(data_frame, data_id, df_tree, verbose=True):
    """Ask questions necessary to identify whether a mushroom is poisonous or edible.
    The questions are based on the decision tree.
    Automatically answered the questions based on the given mushroom data.

    Args:   data_frame (pandas data frame with mushroom data)
            data_id (int, which data to be used)
            tree_df (decision tree as pandas data frame)

    Return: result ('edible' or 'poisonous)
            certainity (float)
    """
    check_next_feat_id = 0
    next_node = 0
    while check_next_feat_id >= 0:
        current_node = next_node
        ask_feat = df_tree.loc[current_node, "feature"]
        ask_val = df_tree.loc[current_node, "feature_value"]
        answ_feat_val = data_frame.loc[data_id, ask_feat]
        desc_val = df_tree.loc[current_node, "feature_description"]
        if answ_feat_val == ask_val:
            next_node = df_tree.loc[current_node, "children_right"]
            check_next_feat_id = df_tree.loc[next_node, "feature_id"]
            if verbose:
                print("The " + ask_feat + " is " + desc_val)
                # debug
                # print('Next with ', next_node)
        else:
            next_node = df_tree.loc[current_node, "children_left"]
            check_next_feat_id = df_tree.loc[next_node, "feature_id"]
            if verbose:
                print("The " + ask_feat + " is not " + desc_val)
                # debug
                # print('Next with ', next_node)
    res = df_tree.loc[next_node, "prediction"]
    cert = df_tree.loc[next_node, "certainity"]
    return res, cert


def can_i_eat_it(df_tree, verbose=True):
    """Ask questions about a mushroom and predicts, based on the answers,
    whether the mushroom is edible. The questions are based on the decision tree.
    Needs user input.
    Args:   tree_df (decision tree as pandas data frame)

    Return: result ('edible' or 'poisonous)
            certainity (float)
    """
    print("Please answer the following questions with yes (y) or no (n).")
    print("-" * 30)
    print(" ")

    check_next_feat_id = 0
    next_node = 0
    while check_next_feat_id >= 0:
        current_node = next_node
        ask_feat = df_tree.loc[current_node, "feature"]
        desc_val = df_tree.loc[current_node, "feature_description"]
        ans = input("Is the " + ask_feat + ": " + desc_val)

        if ans == "y":
            next_node = df_tree.loc[current_node, "children_right"]
            check_next_feat_id = df_tree.loc[next_node, "feature_id"]
            if verbose:
                print("The " + ask_feat + " is " + desc_val)
                # debug
                # print('Next with ', next_node)
        elif ans == "n":
            next_node = df_tree.loc[current_node, "children_left"]
            check_next_feat_id = df_tree.loc[next_node, "feature_id"]
            if verbose:
                print("The " + ask_feat + " is not " + desc_val)
                # debug
                # print('Next with ', next_node)
        else:
            print("Please answer only with y or n.")
    res = df_tree.loc[next_node, "prediction"]
    cert = df_tree.loc[next_node, "certainity"]
    return res, cert


def get_path(id_leaf, df_tree):
    """Get the path along the decision tree which leads to the leaf with
    the given id. Although the function itself goes the path backward, it
    gives the forward path.

    Args:   dictionary with:
            path: path along the id to the leaf
            answers: with answers lead to the leaf

    Return: result ('edible' or 'poisonous)
            certainity (float)
    """
    current_id = id_leaf
    answers = []
    id_path = []
    while current_id != 0:
        # looking from where we get there
        id_path.append(int(current_id))
        answer_no = df_tree[df_tree["children_left"] == current_id].index
        answer_yes = df_tree[df_tree["children_right"] == current_id].index
        if not answer_yes.empty:
            answers.append("y")
            current_id = int(answer_yes[0])
        elif not answer_no.empty:
            answers.append("n")
            current_id = int(answer_no[0])
        else:
            print("ERROR. Should be either yes or no.")
    return {"path": id_path[::-1], "answers": answers[::-1]}
