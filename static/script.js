
const taskInput = document.getElementById("taskInput");
const runButton = document.getElementById("runButton");
const loading = document.getElementById("loading");
const output = document.getElementById("output");
const errorBox = document.getElementById("error");

console.log("NexusAI JavaScript loaded!");

// Show agent result
function addResult(title, content) {
    if (!content || !String(content).trim()) return;

    const card = document.createElement("div");
    card.className = "result-card";

    const heading = document.createElement("h3");
    heading.textContent = title;

    const result = document.createElement("pre");
    result.textContent = content;

    card.appendChild(heading);
    card.appendChild(result);
    output.appendChild(card);
}

// Execute example task on click
async function setTaskAndRun(task) {
    taskInput.value = task;
    await runTask();
}

// Execute user task
async function runTask() {
    const task = taskInput.value.trim();

    if (!task) {
        alert("Please enter a task first.");
        return;
    }

    if (runButton.disabled) return;

    runButton.disabled = true;
    runButton.textContent = "Running...";

    loading.classList.remove("hidden");
    errorBox.classList.add("hidden");
    output.innerHTML = "";

    try {
        const response = await fetch("/api/run", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ task: task })
        });

        const data = await response.json();

        if (!response.ok || !data.success) {
            throw new Error(data.error || "Backend execution failed");
        }

        addResult("Manager Agent", data.category);
        addResult("Research Agent", data.research);
        addResult("Coding Agent", data.code);
        addResult("Testing Agent", data.review);
        addResult("Final Report", data.final);

        if (data.final) {
            const downloadButton = document.createElement("button");
            downloadButton.className = "download-button";
            downloadButton.textContent = "Download Final Report";

            downloadButton.onclick = function () {
                const blob = new Blob([data.final], {
                    type: "text/plain;charset=utf-8"
                });

                const url = URL.createObjectURL(blob);
                const link = document.createElement("a");

                link.href = url;
                link.download = "NexusAI_Report.txt";
                link.click();

                URL.revokeObjectURL(url);
            };

            output.appendChild(downloadButton);
        }

        if (!output.children.length) {
            addResult("NexusAI", "No result was returned.");
        }

        document.getElementById("results").scrollIntoView({
            behavior: "smooth"
        });

    } catch (error) {
        console.error("NexusAI Error:", error);

        errorBox.textContent = "Execution Error: " + error.message;
        errorBox.classList.remove("hidden");

    } finally {
        loading.classList.add("hidden");
        runButton.disabled = false;
        runButton.textContent = "Run NexusAI →";
    }
}

// Ctrl + Enter to run
taskInput.addEventListener("keydown", function(event) {
    if (event.ctrlKey && event.key === "Enter") {
        runTask();
    }
});
