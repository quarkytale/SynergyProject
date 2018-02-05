function [data, h] = plot_nStates(data)

    nSize = length(data(1).q_mean);
    
    for j=1:10
        
        if (j==1)||(j==2)||(j==3)
            name_aux1 = 'human';
        else
            name_aux1 = 'robot';
        end
        
%         if (j==1)||(j==3)
%             name_aux2 = 'x';
%         else
%             name_aux2 = 'y';
%         end
        
        data(j).hq = figurew([name_aux1 '_' num2str(j) ]);
%         data(j).hq = figurew([name_aux1 '_'  name_aux2 '_' num2str(j) ]);
        Hq{j}      = shadedErrorBar([1:nSize], data(j).q_mean , 2*sqrt( data(j).q_var ) , ...
                                  {'g', 'LineWidth', 2'}, 1);
        xlabel 'state index';
        ylabel 'position value';                              

        data(j).hqdot =  figurew([name_aux1 '_dot_', num2str(j)]);
%         data(j).hqdot =  figurew([name_aux1 '_'  name_aux2 'dot_', num2str(j)]);
        Hqdot{j}         = shadedErrorBar([1:nSize], data(j).qdot_mean , 2*sqrt( data(j).qdot_var ) , ...
                                  {'g', 'LineWidth', 2'}, 1);
        xlabel 'state index';
        ylabel 'velocity value';    
        
        
        if 0  % keep only the edges on the plot
            delete(Hq{j}.mainLine);
            delete(Hq{j}.patch);

            delete(Hqdot{j}.mainLine);
            delete(Hqdot{j}.patch); 
        end
        if 1  % keep only the patch
            delete(Hq{j}.mainLine);
            delete(Hq{j}.edge);

            delete(Hqdot{j}.mainLine);
            delete(Hqdot{j}.edge); 
        end
        grid off;
    end
    
    figure( data(1).hq  ); set_fig_position( [0.001 0.506  0.293 0.467]   );
    figure( data(2).hq  ); set_fig_position( [0.333 0.506  0.293 0.467]   );
    figure( data(3).hq  ); set_fig_position( [0.666 0.506  0.293 0.467]   );
    figure( data(4).hq  ); set_fig_position( [0.001 0.0444 0.293 0.467]   );
    figure( data(5).hq  ); set_fig_position( [0.25 0.0444 0.293 0.467]   );
    figure( data(6).hq  ); set_fig_position( [0.5 0.0444 0.293 0.467]   );
    figure( data(7).hq  ); set_fig_position( [0.75 0.0444 0.293 0.467]   );
    figure( data(8).hq  ); set_fig_position( [1.001 0.0444 0.293 0.467]   );
    figure( data(9).hq  ); set_fig_position( [1.333 0.0444 0.293 0.467]   );
    figure( data(10).hq  ); set_fig_position( [1.666 0.0444 0.293 0.467]   );
 
    figure( data(1).hqdot  ); set_fig_position( [0.001 0.506  0.293 0.467]   );
    figure( data(2).hqdot  ); set_fig_position( [0.333 0.506  0.293 0.467]   );
    figure( data(3).hqdot  ); set_fig_position( [0.666 0.506  0.293 0.467]   );
    figure( data(4).hqdot  ); set_fig_position( [0.001 0.0444 0.293 0.467]   );
    figure( data(5).hqdot  ); set_fig_position( [0.25 0.0444 0.293 0.467]   );
    figure( data(6).hqdot  ); set_fig_position( [0.5 0.0444 0.293 0.467]   );
    figure( data(7).hqdot  ); set_fig_position( [0.75 0.0444 0.293 0.467]   );
    figure( data(8).hqdot  ); set_fig_position( [1.001 0.0444 0.293 0.467]   );
    figure( data(9).hqdot  ); set_fig_position( [1.333 0.0444 0.293 0.467]   );
    figure( data(10).hqdot  ); set_fig_position( [1.666 0.0444 0.293 0.467]   );
    
    % handle for figures
    for j=1:length(data)
        h(j).q      = data(j).hq;
        h(j).qshade = [];%Hq{j};
        
        h(j).qdot      = data(j).hqdot;
        h(j).qdotshade = [];%Hqdot{j};        
    end
    
    
    
end