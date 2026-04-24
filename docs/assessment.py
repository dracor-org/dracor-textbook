"""Helpers for self-assessment pages in the DraCor Textbook.

Design goals:
- lightweight HTML widgets that work in Jupyter Book outputs
- no server-side state, no grading, no storage
"""

from __future__ import annotations

from IPython.display import HTML
import json
import uuid


_LOCK_JS = """<script>
(function () {
  if (typeof window.lockAnswer === "function") return;

  window.lockAnswer = function(textareaId) {
    var el = document.getElementById(textareaId);
    if (!el) return;

    // Toggle lock/unlock.
    var isLocked = el.hasAttribute("readonly");

    if (isLocked) {
      el.removeAttribute("readonly");
      el.style.opacity = "1";
    } else {
      el.setAttribute("readonly", "readonly");
      el.style.opacity = "0.75";
    }

    // Update the button label if it follows the naming convention.
    var btn = document.getElementById("btn-" + textareaId);
    if (btn) {
      btn.textContent = isLocked ? "Lock answer" : "Unlock answer";
    }
  };
})();
</script>
"""


def create_answer_box(
    question_id: str,
    rows: int = 4,
    placeholder: str = "Write your answer here…",
    button_label: str = "Lock answer",
) -> HTML:
    """Return a simple textarea + button to support free-text self-assessment.

    - Clicking the button toggles read-only mode (lock/unlock).
    - No data is stored.
    """
    textarea_id = f"answer-{question_id}"
    button_id = f"btn-{textarea_id}"

    html = f"""{_LOCK_JS}
<div style="padding: 6px; border-radius: 6px; margin: 10px 0;">
  <textarea id="{textarea_id}" rows="{rows}"
    style="width: 100%; margin-top: 10px; padding: 10px; border: 1px solid #ced4da; border-radius: 4px;"
    placeholder="{placeholder}"></textarea>
  <button id="{button_id}" onclick="lockAnswer('{textarea_id}')"
    style="margin-top: 6px; padding: 6px 12px; background-color: #00305e; color: white; border: none; border-radius: 4px; cursor: pointer;">
    {button_label}
  </button>
</div>
"""

    return HTML(html)


class DragDropQuiz:
    """
    A simple drag-and-drop quiz generator for Jupyter Books.

    Usage:
    quiz = DragDropQuiz()
    quiz.create_matching_quiz(
        title="Your Quiz Title",
        descriptions=["Description 1", "Description 2", "Description 3"],
        options=["Option A", "Option B", "Option C"],
        correct_mapping={"Description 1": "Option A", "Description 2": "Option B", "Description 3": "Option C"}
    )
    """

    def __init__(self):
        self.quiz_counter = 0

    def create_matching_quiz(self, title, descriptions, options, correct_mapping, show_feedback=True, feedback_messages=None):
        """
        Create a drag-and-drop matching quiz.

        Parameters:
        - title (str): The quiz title/question
        - descriptions (list): List of items to be matched (static labels)
        - options (list): List of draggable options (draggable items)
        - correct_mapping (dict): Dictionary mapping descriptions to correct options
        - show_feedback (bool): Whether to show feedback after submission
        - feedback_messages (dict): Custom feedback messages with keys 'correct', 'incorrect', 'partial'
        """
        self.quiz_counter += 1
        quiz_id = f"drag_drop_quiz_{self.quiz_counter}_{uuid.uuid4().hex[:8]}"

        # Set default feedback messages if none provided
        if feedback_messages is None:
            feedback_messages = {
                "correct": "Perfect! All {total} answers are correct!",
                "incorrect": "None of the answers are correct. Please try again!",
                "partial": "Partially correct: {correct} out of {total} answers are correct."
            }

        # Convert correct mapping to use indices for easier JavaScript handling
        desc_to_idx = {desc: i for i, desc in enumerate(descriptions)}
        opt_to_idx = {opt: i for i, opt in enumerate(options)}

        correct_pairs = []
        for desc, opt in correct_mapping.items():
            if desc in desc_to_idx and opt in opt_to_idx:
                correct_pairs.append([desc_to_idx[desc], opt_to_idx[opt]])

        html_content = self._generate_html(
            quiz_id, title, descriptions, options, correct_pairs, show_feedback, feedback_messages
        )

        return HTML(html_content)

    def _generate_html(self, quiz_id, title, descriptions, options, correct_pairs, show_feedback, feedback_messages):
        """Generate the complete HTML for the drag-and-drop quiz."""

        # Generate static description labels with drop zones
        description_zones = ""
        for i, desc in enumerate(descriptions):
            description_zones += f'''
                <div class="description-zone">
                    <div class="description-label">{desc}</div>
                    <div class="drop-area" data-zone-id="{i}" id="{quiz_id}_drop_{i}">
                        <span class="drop-placeholder">Drop here.</span>
                    </div>
                </div>
            '''

        # Generate draggable options
        draggable_options = ""
        for i, option in enumerate(options):
            draggable_options += f'''
                <div class="draggable-option" draggable="true" data-item-id="{i}" id="{quiz_id}_option_{i}">
                    {option}
                </div>
            '''

        return f'''
        <style>
            .drag-drop-quiz {{
                padding: 15px;
                border: 1px solid #ddd;
                border-radius: 6px;
                margin: 15px 0;
                font-family: sans-serif;
            }}
            .quiz-title {{
                font-size: 18px;
                font-weight: bold;
                margin-bottom: 15px;
            }}
            .quiz-main {{
                margin-bottom: 20px;
            }}
            .descriptions-container {{
                display: grid;
                gap: 10px;
            }}
            .description-zone {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 10px;
                align-items: start;
            }}
            .description-label {{
                padding: 10px;
                background: #f5f5f5;
                border-radius: 4px;
                font-weight: 500;
            }}
            .drop-area {{
                min-height: 40px;
                padding: 10px;
                background: #e8f5e9;
                border: 2px dashed #4caf50;
                border-radius: 4px;
                display: flex;
                align-items: center;
                justify-content: center;
            }}
            .drop-area.filled {{
                border-style: solid;
                background: #c8e6c9;
            }}
            .drop-placeholder {{
                color: #888;
                font-size: 12px;
            }}
            .options-container {{
                margin-bottom: 15px;
                padding: 10px;
                background: #fafafa;
                border-radius: 4px;
            }}
            .options-title {{
                font-size: 14px;
                margin-bottom: 10px;
                color: #666;
            }}
            .options-list {{
                display: flex;
                flex-wrap: wrap;
                gap: 10px;
            }}
            .draggable-option {{
                padding: 10px 15px;
                background: #2196F3;
                color: white;
                border-radius: 4px;
                cursor: move;
                user-select: none;
                border: 2px solid #1976D2;
            }}
            .draggable-option:hover {{
                background: #1976D2;
            }}
            .draggable-option.dragging {{
                opacity: 0.5;
            }}
            .quiz-controls {{
                margin-top: 15px;
                display: flex;
                gap: 10px;
            }}
            .quiz-button {{
                padding: 8px 16px;
                background-color: #00305e;
                color: white;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                font-size: 14px;
            }}
            .quiz-button:hover {{
                background-color: #00205e;
            }}
            .reset-button {{
                background-color: #666;
            }}
            .reset-button:hover {{
                background-color: #555;
            }}
            #{{quiz_id}}_feedback {{
                margin-top: 15px;
                padding: 10px;
                border-radius: 4px;
                font-weight: bold;
                display: none;
            }}
            #{{quiz_id}}_feedback.correct {{
                background: #d4edda;
                color: #155724;
                border: 1px solid #c3e6cb;
                display: block;
            }}
            #{{quiz_id}}_feedback.incorrect {{
                background: #f8d7da;
                color: #721c24;
                border: 1px solid #f5c6cb;
                display: block;
            }}
            #{{quiz_id}}_feedback.partial {{
                background: #fff3cd;
                color: #856404;
                border: 1px solid #ffeeba;
                display: block;
            }}
        </style>

        <div class="drag-drop-quiz" id="{quiz_id}">
            <div class="quiz-title">{title}</div>

            <div class="quiz-main">
                <div class="descriptions-container">
                    {description_zones}
                </div>
            </div>

            <div class="options-container">
                <div class="options-title">Drag and drop the elements to the correct statements.</div>
                <div class="options-list" id="{quiz_id}_options">
                    {draggable_options}
                </div>
            </div>

            <div class="quiz-controls">
                <button class="quiz-button" onclick="checkAnswer_{quiz_id}()">Check the answer.</button>
                <button class="quiz-button reset-button" onclick="resetQuiz_{quiz_id}()">Reset.</button>
            </div>

            <div id="{quiz_id}_feedback"></div>
        </div>

        <script>
            // Initialize drag-drop functionality
            document.addEventListener('DOMContentLoaded', function() {{
                const quiz_id = '{quiz_id}';
                const correct_pairs = {json.dumps(correct_pairs)};
                const feedback_messages = {json.dumps(feedback_messages)};
                let dragged_item = null;

                // Setup drag handlers
                document.addEventListener('dragstart', function(e) {{
                    if (e.target.classList.contains('draggable-option')) {{
                        dragged_item = e.target;
                        e.target.classList.add('dragging');
                        e.dataTransfer.effectAllowed = 'move';
                    }}
                }});

                document.addEventListener('dragend', function(e) {{
                    if (e.target.classList.contains('draggable-option')) {{
                        e.target.classList.remove('dragging');
                        dragged_item = null;
                    }}
                }});

                document.addEventListener('dragover', function(e) {{
                    if (e.target.classList.contains('drop-area')) {{
                        e.preventDefault();
                        e.dataTransfer.dropEffect = 'move';
                    }}
                }});

                document.addEventListener('drop', function(e) {{
                    if (e.target.classList.contains('drop-area') && dragged_item) {{
                        e.preventDefault();
                        const existing = e.target.querySelector('.draggable-option');
                        if (existing) {{
                            document.getElementById(quiz_id + '_options').appendChild(existing);
                        }}
                        e.target.appendChild(dragged_item);
                        e.target.classList.add('filled');
                        dragged_item = null;
                    }}
                }});

                // Check answer function
                window['checkAnswer_' + quiz_id] = function() {{
                    const feedback_el = document.getElementById(quiz_id + '_feedback');
                    let correct_count = 0;

                    correct_pairs.forEach(pair => {{
                        const desc_idx = pair[0];
                        const opt_idx = pair[1];
                        const drop_zone = document.getElementById(quiz_id + '_drop_' + desc_idx);
                        const draggable = drop_zone.querySelector('.draggable-option');

                        if (draggable && parseInt(draggable.dataset.itemId) === opt_idx) {{
                            correct_count++;
                        }}
                    }});

                    const total = correct_pairs.length;
                    feedback_el.innerHTML = '';
                    feedback_el.classList.remove('correct', 'incorrect', 'partial');

                    if (correct_count === total) {{
                        feedback_el.textContent = feedback_messages.correct.replace('{{total}}', total);
                        feedback_el.classList.add('correct');
                    }} else if (correct_count === 0) {{
                        feedback_el.textContent = feedback_messages.incorrect;
                        feedback_el.classList.add('incorrect');
                    }} else {{
                        feedback_el.textContent = feedback_messages.partial.replace('{{correct}}', correct_count).replace('{{total}}', total);
                        feedback_el.classList.add('partial');
                    }}
                }};

                // Reset function
                window['resetQuiz_' + quiz_id] = function() {{
                    // Move all draggables back to options container
                    const drops = document.querySelectorAll('[id^="' + quiz_id + '_drop_"]');
                    const options_container = document.getElementById(quiz_id + '_options');

                    drops.forEach(drop => {{
                        const draggable = drop.querySelector('.draggable-option');
                        if (draggable) {{
                            options_container.appendChild(draggable);
                        }}
                        drop.classList.remove('filled');
                    }});

                    const feedback_el = document.getElementById(quiz_id + '_feedback');
                    feedback_el.innerHTML = '';
                    feedback_el.classList.remove('correct', 'incorrect', 'partial');
                }};
            }});
        </script>
        '''
