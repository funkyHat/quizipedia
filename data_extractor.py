import json

def get_file(path):
    with open(path, "rt") as f:
        return "".join(f.readlines())


source = json.loads(get_file('./example_table.json'))


def build_question(source):
    # print(source)

    headings = set()
    for row in source:
        for k in row.keys():
            headings.add(k)

    # print(headings)

    def all_values(heading):
        result = set()
        for row in source:
            if heading in row:
                result.add(row[heading])
        return result

    options = {heading: all_values(heading) for heading in headings}

    # import pprint
    # pprint.pprint(options)

    import random
    question = random.choice(list(source))

    # print(question)
    contexts = ["Song"]
    queries = ["Year", "Artist"]

    def choose_query(queries):
        query = random.choice(queries)
        possible = options[query]
        answer = question[query]
        return query, [question[query]] + sorted(p for p in possible if p != answer)

    def choose_context(contexts):
        context = random.choice(contexts)
        return context, question[context]

    question_bundle = {}

    query, value = choose_query(queries)
    # print('x: {}'.format(choose_query(queries)))

    context, c_value = choose_context(contexts)
    # print('y: {}'.format(choose_context(contexts)))

    question_bundle[context] = c_value
    question_bundle['query'] = query
    question_bundle['answers'] = value

    print(question_bundle)
    return question_bundle

build_question(source)