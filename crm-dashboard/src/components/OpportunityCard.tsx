'use client';

import { Opportunity } from '@/lib/api';

interface OpportunityCardProps {
    opportunity: Opportunity;
    onDragStart: (e: React.DragEvent, opp: Opportunity) => void;
    onClick?: (opp: Opportunity) => void;
}

export default function OpportunityCard({ opportunity, onDragStart, onClick }: OpportunityCardProps) {
    const formatCurrency = (value: number) => {
        return new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'USD',
            minimumFractionDigits: 0,
            maximumFractionDigits: 0,
        }).format(value);
    };

    const stageClass = opportunity.stage.toLowerCase().replace(/\s+/g, '-');

    return (
        <div
            className={`opp-card border-l-4 stage-${stageClass} animate-fade-in`}
            draggable
            onDragStart={(e) => onDragStart(e, opportunity)}
            onClick={() => onClick?.(opportunity)}
        >
            <div className="flex justify-between items-start mb-2">
                <h4 className="font-medium text-sm text-zinc-100 line-clamp-2">
                    {opportunity.title}
                </h4>
            </div>

            <div className="text-xs text-zinc-400 mb-2">
                {opportunity.lead?.company_name || 'Unknown Company'}
            </div>

            <div className="flex justify-between items-center">
                <span className="text-lg font-semibold text-green-400">
                    {formatCurrency(opportunity.value)}
                </span>
                <span className="text-xs text-zinc-500 bg-zinc-800 px-2 py-1 rounded">
                    {opportunity.probability}%
                </span>
            </div>

            {opportunity.close_date && (
                <div className="text-xs text-zinc-500 mt-2">
                    Close: {new Date(opportunity.close_date).toLocaleDateString()}
                </div>
            )}
        </div>
    );
}
