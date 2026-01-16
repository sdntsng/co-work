'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';
import ThemeToggle from './ThemeToggle';

const navItems = [
    { href: '/', label: 'Dashboard', icon: '📊' },
    { href: '/pipeline', label: 'Pipeline', icon: '🎯' },
    { href: '/leads', label: 'Leads', icon: '👥' },
];

export default function Sidebar() {
    const pathname = usePathname();

    return (
        <aside className="w-64 min-h-screen sidebar flex flex-col transition-colors duration-300">
            {/* Logo */}
            <div className="p-6 border-b border-[var(--border)] flex justify-between items-center">
                <h1 className="text-xl font-serif font-bold text-[var(--accent)] tracking-tight">
                    Vinci CRM
                </h1>
                <ThemeToggle />
            </div>

            {/* Navigation */}
            <nav className="flex-1 p-4">
                <ul className="space-y-2">
                    {navItems.map(item => (
                        <li key={item.href}>
                            <Link
                                href={item.href}
                                className={`flex items-center gap-3 px-4 py-3 rounded-lg transition-all sidebar-link ${pathname === item.href
                                    ? 'active font-medium shadow-sm'
                                    : ''
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
            <div className="p-4 border-t border-[var(--border)]">
                <p className="text-xs text-zinc-600 text-center">
                    Powered by Google Sheets
                </p>
            </div>
        </aside>
    );
}
