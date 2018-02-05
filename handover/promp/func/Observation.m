classdef Observation < handle
   
   properties
      set;
      joint;
      jointvel;
      index;
      stdev;
      q;
      qdot;
   end    
    
methods

    function obj = Observation(set, stdev, param)
        obj.set = set;
        obj.joint = param.observedJointPos;
        obj.jointvel = param.observedJointVel;
        obj.stdev = stdev;   
        % prepare the vector of observations by filling it with zeros
        for j = 1:param.nTotalJoints
            obj.q(j,:) = 0.*ones(1, param.nTraj);
            obj.qdot(j,:) = 0.*ones(1, param.nTraj);
        end
        
    end

%     function obj = measuredIndexes(obj, index, data)
    function obj = measuredIndexes(obj, index, data, point)
        obj.index = index;
        for j = obj.joint
            obj.q(j,index)    = point(j);
%             obj.q(j,index)    = data(j).q(obj.set, index);   
        end
        for j = obj.jointvel
            obj.qdot(j,index) = data(j).qdot(obj.set, index);
        end
    end

end %methods

end


