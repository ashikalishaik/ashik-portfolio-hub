export default function Projects() {
  return (
    <section id="projects" className="max-w-6xl mx-auto px-6 py-20">
      <h2 className="text-3xl font-bold mb-8">Projects</h2>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

        <div className="border border-slate-700 p-6 rounded-xl bg-slate-900">
          <h3 className="text-xl font-semibold">Time Series Forecasting</h3>
          <p className="text-slate-300 mt-2">
            Built SARIMA-based forecasting pipeline with evaluation metrics
            (MAE, RMSE) and visual trend-seasonal decomposition.
          </p>
        </div>

        <div className="border border-slate-700 p-6 rounded-xl bg-slate-900">
          <h3 className="text-xl font-semibold">AI Call Agent</h3>
          <p className="text-slate-300 mt-2">
            AI-driven automated voice response system using LLM + Twilio +
            backend automation workflows.
          </p>
        </div>

      </div>
    </section>
  );
}
