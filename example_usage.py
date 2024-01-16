from graph_word_processor import GraphWaveformProcessor

# Example Usage:
# Assuming your graph is represented as a dictionary where keys are node IDs and values are node vectors
sample_graph = {
    1: np.array([1.0, 2.0, 3.0]),
    2: np.array([4.0, 5.0, 6.0]),
    3: np.array([7.0, 8.0, 9.0]),
}

graph_processor = GraphWaveformProcessor(sample_graph)

# Example 1: Get the waveform for node 1
waveform_1 = graph_processor.node_waveform(1)
print("Waveform for Node 1:", waveform_1)

# Example 2: Sum the waveforms of nodes 1 and 2
subset_waveform = graph_processor.subset_sum_waveform([1, 2])
print("Summed Waveform for Nodes 1 and 2:", subset_waveform)

# Example 3: Error correct the waveform
error_corrected_waveform = graph_processor.error_correct_waveform(subset_waveform)
print("Error Corrected Waveform:", error_corrected_waveform)

# Example 4: Represent the error corrected waveform
representation = graph_processor.represent_error_corrected_waveform(error_corrected_waveform)
print("Representation of Error Corrected Waveform:", representation)
