# Graph Waveform Processor

This Python class provides a basic implementation for representing and manipulating waveforms in the context of graph theory and vector distances. It includes functionality for computing node waveforms, summing waveforms of nodes in a subset, error correcting waveforms, and representing the error-corrected waveform.


We consider a graph in which we know the vectors of several frames for all nodes. We assume that all nodes in this graph are entangled.

In our example_usage.py file, we first initialize our class with the sample_graph. 
Then we demonstrate getting the waveform of one node. After which, we demonstrate adding a subset of waveforms together. 
Finally, we get the error corrected waveform using an arbitrary filter. 

## Installation:
   Clone the repository to your local machine.

 ```bash
 git clone https://github.com/cobycloud/graph-waveform-processor.git
```

## Example Usage:

```python
from graph_waveform_processor import GraphWaveformProcessor

# Assuming your graph is represented as a dictionary where keys are node IDs and values are node vectors
sample_graph = {
    1: np.array([1.0, 2.0, 3.0]),
    2: np.array([4.0, 5.0, 6.0]),
    3: np.array([7.0, 8.0, 9.0]),
}

graph_processor = GraphWaveformProcessor(sample_graph)

# Example: Get the waveform for node 1
waveform_1 = graph_processor.node_waveform(1)
print("Waveform for Node 1:", waveform_1)

```

## Savitzky-Golay Filter:
The Savitzky-Golay filter is applied in the error correction step (error_correct_waveform). It is a signal processing filter that smoothens and removes noise from the waveform. The window_size and polyorder parameters can be adjusted to fine-tune the denoising effect.

## Benefits of Error Corrected Waveform
- Improved Accuracy: The error-corrected waveform provides a more accurate representation of the underlying relationships in the system by reducing noise.
- Enhanced Signal Quality: The denoising effect results in a cleaner and more refined waveform, contributing to better signal quality.
- Robustness: A waveform less susceptible to errors is more robust in the face of variations or disturbances in the data.
- Facilitates Analysis: Clean and accurate waveforms are conducive to more effective analysis, aiding in extracting meaningful insights from the data.

## Customization:

- Replace the sample graph with your own graph representation logic.
- Modify the error correction method according to your specific requirements.

## Contribution:
Contributions are welcome! Feel free to open issues or pull requests.
