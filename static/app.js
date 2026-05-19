
let questions = [];
let currentIndex = 0;
let score = 0;
let usedHints = 0;
let answers = [];
let currentChecked = null;

const POINTS = 10;
const STORAGE_KEY = "check_do_golpe_progress_v1";

function $(id) { return document.getElementById(id); }

function show(screenId) {
    document.querySelectorAll(".screen").forEach(s => s.classList.remove("active"));
    $(screenId).classList.add("active");
}

async function loadQuestions() {
    const res = await fetch("/api/questions");
    questions = await res.json();
    $("totalQuestions").textContent = questions.length;
    const saved = localStorage.getItem(STORAGE_KEY);
    if (saved) {
        try {
            const data = JSON.parse(saved);
            if (data.currentIndex > 0 && data.currentIndex < questions.length) {
                if (confirm("Existe um progresso salvo. Deseja continuar?")) {
                    currentIndex = data.currentIndex || 0;
                    score = data.score || 0;
                    usedHints = data.usedHints || 0;
                    answers = data.answers || [];
                    renderQuestion();
                }
            }
        } catch(e) {}
    }
}

function saveLocal() {
    localStorage.setItem(STORAGE_KEY, JSON.stringify({ currentIndex, score, usedHints, answers, savedAt: Date.now() }));
}

function startQuiz() {
    currentIndex = 0;
    score = 0;
    usedHints = 0;
    answers = [];
    localStorage.removeItem(STORAGE_KEY);
    renderQuestion();
}

function renderQuestion() {
    if (currentIndex >= questions.length) return showResult();
    currentChecked = null;
    const q = questions[currentIndex];

    $("questionCounter").textContent = `Questão ${currentIndex + 1}/${questions.length}`;
    $("progressBar").style.width = `${((currentIndex + 1) / questions.length) * 100}%`;
    $("scoreNow").textContent = score;
    $("fakeUrl").value = q.url;
    $("storeName").textContent = q.store;
    $("productImage").textContent = q.image;
    $("productName").textContent = q.product;
    $("price").textContent = q.price || "Atenção aos dados solicitados";
    $("payment").textContent = q.payment;
    $("questionTitle").textContent = q.title;
    $("hintBox").classList.add("hidden");
    $("hintBox").textContent = "";
    show("questionScreen");
    saveLocal();
}

function showHint() {
    const q = questions[currentIndex];
    if ($("hintBox").classList.contains("hidden")) {
        usedHints += 1;
        $("hintBox").textContent = "💡 Dica: " + q.hint;
        $("hintBox").classList.remove("hidden");
        saveLocal();
    }
}

async function answerQuestion(answer) {
    const q = questions[currentIndex];
    const res = await fetch("/api/check", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({id: q.id, answer})
    });
    const result = await res.json();
    currentChecked = result;

    if (result.correct) score += POINTS;

    answers.push({
        id: q.id,
        answer,
        correct: result.correct,
        correctAnswer: result.correctAnswer,
        usedHint: !$("hintBox").classList.contains("hidden")
    });

    $("feedbackTop").className = "feedback-top " + (result.correct ? "feedback-ok" : "feedback-bad");
    $("feedbackIcon").textContent = result.correct ? "✅" : "❌";
    $("feedbackTitle").textContent = result.correct ? "Correto! Era " + result.correctAnswer + "!" : "Ops! Era " + result.correctAnswer + "!";
    $("feedbackSubtitle").textContent = result.correct ? "O que você identificou:" : "Por que a resposta correta é essa:";
    $("signalsList").innerHTML = result.signals.map(s => `<span>${s}</span>`).join("");
    $("feedbackText").textContent = result.explanation;
    $("feedbackScore").textContent = score;
    currentIndex += 1;
    saveLocal();
    show("feedbackScreen");
}

function nextQuestion() {
    renderQuestion();
}

async function showResult() {
    const correct = answers.filter(a => a.correct).length;
    const total = questions.length;
    const percent = Math.round((correct / total) * 100);

    $("finalScore").textContent = score;
    $("finalCorrect").textContent = correct;
    $("finalTotal").textContent = total;
    $("finalPercent").textContent = percent;
    $("resultCorrect").textContent = correct;
    $("resultErrors").textContent = total - correct;
    $("resultHints").textContent = usedHints;

    let msg = "Continue praticando para reconhecer golpes com mais segurança.";
    if (percent >= 80) msg = "Parabéns, você está preparado! Continue praticando para manter sua proteção digital.";
    else if (percent >= 50) msg = "Bom resultado! Revise os sinais de URL, preço e forma de pagamento.";
    $("performanceMessage").textContent = msg;

    localStorage.removeItem(STORAGE_KEY);
    show("resultScreen");

    try {
        await fetch("/api/attempts", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({ score, total, percent, usedHints, answers })
        });
    } catch(e) {}
}

function restartQuiz() {
    startQuiz();
}

function goHome() {
    show("startScreen");
}

function showAuth() {
    show("authScreen");
    showHistory();
}

async function signup() {
    authRequest("/api/signup");
}

async function login() {
    authRequest("/api/login");
}

async function authRequest(url) {
    const email = $("email").value;
    const password = $("password").value;
    const res = await fetch(url, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({email, password})
    });
    const data = await res.json();
    $("authMessage").textContent = data.error || ("Conectado como " + data.email);
    if (!data.error) showHistory();
}

async function showHistory() {
    const box = $("historyList");
    try {
        const res = await fetch("/api/attempts");
        const data = await res.json();
        if (data.error) {
            box.textContent = "Entre na conta para ver seu histórico.";
            return;
        }
        if (!data.length) {
            box.textContent = "Nenhuma tentativa salva ainda.";
            return;
        }
        box.innerHTML = data.map(item => {
            const d = new Date(item.created_at).toLocaleString("pt-BR");
            return `<div class="history-item"><b>${item.score} pontos</b> — ${item.percent}%<br><small>${d} • ${item.used_hints} dica(s)</small></div>`;
        }).join("");
    } catch(e) {
        box.textContent = "Histórico indisponível no momento.";
    }
}

if ("serviceWorker" in navigator) {
    navigator.serviceWorker.register("/static/service-worker.js").catch(() => {});
}

loadQuestions();
