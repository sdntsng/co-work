'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';

const navItems = [
    { href: '/', label: 'Dashboard', icon: '📊' },
    { href: '/pipeline', label: 'Pipeline', icon: '🎯' },
    { href: '/leads', label: 'Leads', icon: '👥' },
];

export default function Sidebar() {
    const pathname = usePathname();

    return (
        <aside className="w-64 min-h-screen bg-zinc-950 border-r border-zinc-800 flex flex-col">
            {/* Logo */}
            <div className="p-6 border-b border-zinc-800">
                <h1 className="text-xl font-bold bg-gradient-to-r from-indigo-400 to-purple-400 bg-clip-text text-transparent">
                    Sales Pipeline 2026
                </h1>
            </div>

            {/* Navigation */}
            <nav className="flex-1 p-4">
                <ul className="space-y-2">
                    {navItems.map(item => (
                        <li key={item.href}>
                            <Link
                                href={item.href}
                                className={`flex items-center gap-3 px-4 py-3 rounded-lg transition-all ${pathname === item.href
                                        ? 'bg-indigo-500/10 text-indigo-400 border border-indigo-500/30'
                                        : 'text-zinc-400 hover:bg-zinc-800 hover:text-zinc-100'
                                    }`}
                            >
                                <span>{item.icon}</span>
                                <span className="font-medium">{item.label}</span>
                            </Link>
                        </li>
                    ))}
                </ul>
            </nav>

            {/* Footer */}
            <div className="p-4 border-t border-zinc-800">
                <p className="text-xs text-zinc-600 text-center">
                    Powered by Google Sheets
                </p>
            </div>
        </aside>
    );
}
