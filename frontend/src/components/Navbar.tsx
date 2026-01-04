export default function Navbar() {
  return (
    <nav className="border-b border-slate-700/50 sticky top-0 bg-slate-950/90 backdrop-blur">
      <div className="max-w-6xl mx-auto px-6 py-4 flex justify-between items-center">
        <h1 className="text-xl font-bold">
          Ashik <span className="text-indigo-400">Portfolio</span>
        </h1>

        <div className="space-x-6 text-slate-300">
          <a href="#projects" className="hover:text-white">Projects</a>
          <a href="#experience" className="hover:text-white">Experience</a>
          <a href="#contact" className="hover:text-white">Contact</a>
        </div>
      </div>
    </nav>
  );
}
