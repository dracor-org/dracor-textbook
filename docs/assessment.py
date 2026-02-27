"""Helpers for self-assessment pages in the DraCor Textbook.

Design goals:
- lightweight HTML widgets that work in Jupyter Book outputs
- no server-side state, no grading, no storage
"""

from __future__ import annotations

from IPython.display import HTML


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
