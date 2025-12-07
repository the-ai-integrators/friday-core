from friday.graphs.sample_graph import create_simple_graph

def main():
    graph = create_simple_graph()

    user_input = "Tokyo"
    state = {"input": user_input}

    print("===== Friday-Core Demo Start =====")
    result = graph.invoke(state)
    print(result)
    print("===== Demo Completed =====")

if __name__ == "__main__":
    main()
