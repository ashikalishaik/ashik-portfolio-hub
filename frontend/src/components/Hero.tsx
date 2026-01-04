export default function Hero() {
  return (
    <section className="max-w-6xl mx-auto px-6 py-32">
      <p className="text-indigo-400 mb-3">Hi, I am</p>

      <h1 className="text-5xl font-bold leading-tight">
        Ashik Ali <span className="text-indigo-400">Shaik</span>
      </h1>

      <p className="text-slate-300 mt-6 text-lg max-w-2xl">
        I am a Computer Engineering graduate focused on AI, Machine Learning,
        secure systems, and building meaningful real-world applications.
      </p>

      <div className="mt-8 space-x-4">
        <a
          href="#projects"
          className="bg-indigo-600 hover:bg-indigo-700 px-6 py-3 rounded-lg"
        >
          View Projects
        </a>

        <a
          href="#contact"
          className="border border-slate-600 hover:border-white px-6 py-3 rounded-lg"
        >
          Contact Me
        </a>
      </div>
    </section>
  );
}
